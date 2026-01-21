from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('agents', views.agents, name='agents'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('properties', views.properties, name='properties'),
]
