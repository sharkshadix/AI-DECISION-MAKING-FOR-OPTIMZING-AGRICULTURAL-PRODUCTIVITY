from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crop-recommendation/', views.crop_recommendation, name='crop_recommendation'),
    path('fertilizer-suggestion/', views.fertilizer_suggestion, name='fertilizer_suggestion'),
    path('disease-detection/', views.disease_detection, name='disease_detection'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('crop-recommendation/', views.crop_recommendation, name='crop_recommendation'),
]

