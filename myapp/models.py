from django.db import models

# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    medical_history = models.TextField()
    dob = models.DateField()

    def __str__(self):
        return self.firstname

class Doctor(models.Model):
    fullname = models.CharField(max_length=100)
    doctorid = models.IntegerField()
    age= models.IntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

 # 5ward model(name,capacity,department,floor
class Ward(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    department = models.CharField(max_length=100)
    floor = models.IntegerField()

    def __str__(self):
        return self.name



