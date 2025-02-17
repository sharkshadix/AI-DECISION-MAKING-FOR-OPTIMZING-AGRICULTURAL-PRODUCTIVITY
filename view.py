from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crop-recommendation/', views.crop_recommendation, name='crop_recommendation'),
    path('fertilizer-suggestion/', views.fertilizer_suggestion, name='fertilizer_suggestion'),
    path('disease-detection/', views.disease_detection, name='disease_detection'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def crop_recommendation(request):
    return render(request, 'crop_recommendation.html')

def fertilizer_suggestion(request):
    return render(request, 'fertilizer_suggestion.html')

def disease_detection(request):
    return render(request, 'disease_detection.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')