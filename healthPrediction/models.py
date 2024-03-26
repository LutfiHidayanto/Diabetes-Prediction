
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.db.models.functions import Cast

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return f"{self.username} {self.first_name}"
    

class diabetesPrediction(models.Model):
    # Categorical features
    Diabetes_binary = models.BooleanField(default=False)
    HighBP = models.BooleanField(default=False)
    HighChol = models.BooleanField(default=False)
    CholCheck = models.BooleanField(default=False)
    Smoker = models.BooleanField(default=False)
    Stroke = models.BooleanField(default=False)
    HeartDiseaseorAttack = models.BooleanField(default=False)
    PhysActivity = models.BooleanField(default=False)
    Fruits = models.BooleanField(default=False)
    Veggies = models.BooleanField(default=False)
    HvyAlcoholConsump = models.BooleanField(default=False)
    AnyHealthcare = models.BooleanField(default=False)
    NoDocbcCost = models.BooleanField(default=False)
    DiffWalk = models.BooleanField(default=False)
    Sex = models.BooleanField(default=False)

    # Non-categorical features
    BMI = models.FloatField(default=0.0)
    GenHlth = models.FloatField(default=0.0)
    MentHlth = models.FloatField(default=0.0)
    PhysHlth = models.FloatField(default=0.0)
    Age = models.FloatField(default=0.0)