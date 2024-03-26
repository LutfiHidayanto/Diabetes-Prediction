from django.shortcuts import render
from .forms import diabetesPredictionForm
from .preprocessing import loadModel, scaleData, predict, convertFormData
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from .models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def diabetes_view(request):
    result = ""
    if request.method == 'POST':
        form = diabetesPredictionForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            data = cleaned_data.items()

            data = convertFormData(data)
            print(data.head())

            data = scaleData(data)

            if data is None:
                return HttpResponse("Scaling data error")
            model = loadModel('healthPrediction/static/healthPrediction/models/xgboost_diabetes.pickle')
            if model is None:
                return HttpResponse("Loading model error")
            prediction = predict(data, model)
            if prediction == None:
                return Http404("Prediction Error")
            
            print(prediction)
            result = prediction[0]
            print(type(result))
    else:
        form = diabetesPredictionForm()
    return render(request, 'healthPrediction/diabetes.html', {
        'form': form,
        'result': result
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "healthPrediction/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "healthPrediction/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "healthPrediction/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "healthPrediction/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "healthPrediction/register.html")