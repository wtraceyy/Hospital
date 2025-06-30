from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def starter(request):
    return render(request,"starter-page.html")

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"services.html")

def doctors(request):
    return render(request,"doctors.html")

def appointment(request):
    return render(request,"appointment.html")

def department(request):
    return render(request,"departments.html")



