from django.contrib import admin
from django.urls import path
from . import views #period(.) represents current folder "myapp"

urlpatterns = [

    path('home/', views.index, name='Home'),
    path('starter/', views.starter, name='Start'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('department/', views.department, name='department'),
]
