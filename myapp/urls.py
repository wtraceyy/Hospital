from django.contrib import admin
from django.urls import path
from . import views #period(.) represents current folder "myapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='Home'),
    path('starter/', views.starter, name='Start'),
    path('about/', views.about, name='About'),
    path('service/', views.service, name='Services'),
    path('doctors/', views.doctors, name='Doctors'),
    path('appointment/', views.appointment, name='Appointment'),
    path('department/', views.department, name='Departments'),
]
