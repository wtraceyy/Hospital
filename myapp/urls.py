from django.contrib import admin
from django.urls import path
from . import views #period(.) represents current folder "myapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Home'),
    path('starter/', views.starter, name='Start'),
]
