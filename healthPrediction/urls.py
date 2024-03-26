from django.urls import path
from . import views

urlpatterns = [
    path('', views.diabetes_view, name="diabetes-view"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]
