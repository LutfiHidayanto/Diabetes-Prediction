from django import forms
from .models import diabetesPrediction

class diabetesPredictionForm(forms.ModelForm):
    class Meta:
        model = diabetesPrediction
        exclude = ['Diabetes_binary']
        labels = {
            'HighBP': 'High Blood Pressure',
            'HighChol': 'High Cholesterol',
            'CholCheck': 'Cholesterol Check',
            'Smoker': 'Smoker',
            'Stroke': 'Stroke',
            'HeartDiseaseorAttack': 'Heart Disease or Attack',
            'PhysActivity': 'Physical Activity',
            'Fruits': 'Fruits Consumption',
            'Veggies': 'Vegetables Consumption',
            'HvyAlcoholConsump': 'Heavy Alcohol Consumption',
            'AnyHealthcare': 'Any Healthcare',
            'NoDocbcCost': 'No Doctor Due to Cost',
            'DiffWalk': 'Difficulty Walking',
            'Sex': 'Sex',
            'BMI': 'Body Mass Index',
            'GenHlth': 'General Health(1-5)',
            'MentHlth': 'Mental Health(0-30)',
            'PhysHlth': 'Physical Health(0-30)',
            'Age': 'Age'
        }