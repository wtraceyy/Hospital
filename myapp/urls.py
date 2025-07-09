from django.contrib import admin
from django.urls import path
from . import views #period(.) represents current folder "myapp"

urlpatterns = [

    path('home/', views.index, name='Home'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('starter/', views.starter, name='Start'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('department/', views.department, name='department'),
    path('contact/', views.contact, name='contact'),
    path('show/', views.show, name='show'),
    path('showcontact/', views.show_contact, name='showcontact'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete),
]
