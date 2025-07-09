from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib import messages
from django.contrib.auth.models import User


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
    if request.method == "POST":
        myappointments = Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            datetime = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message']
        )
        myappointments.save()
        messages.success(request, "Your appointment has been created")
        return redirect('/show')

    else:
        return render(request,"appointment.html")

def department(request):
    return render(request,'department.html')

def contact(request):
    if request.method == "POST":
        mycontacts = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        mycontacts.save()
        messages.warning(request, "Your contact has been created")
        return redirect('/contact')

    else:
        return render(request,"contact.html")

def show(request):
    all = Appointment.objects.all()
    return render(request, 'show.html',{'all':all})

def delete(request,id):
    myappoint = Appointment.objects.get(id=id)
    myappoint.delete()
    return redirect('/show')

def show_contact(request):
    all_times = Contact.objects.all()
    return render(request, 'showcontact.html', {'all': all_times})

def delete(request,id):
    mycontact = Contact.objects.get(id=id)
    mycontact.delete()
    return redirect('/showcontact')

def edit(request,id):
   editappointment= get_object_or_404(Appointment,id=id)

   if request.method == "POST":
       editappointment.name = request.POST.get('name')
       editappointment.email = request.POST.get('email')
       editappointment.phone = request.POST.get('phone')
       editappointment.datetime = request.POST.get('date')
       editappointment.department = request.POST.get('department')
       editappointment.doctor = request.POST.get('doctor')
       editappointment.message = request.POST.get('message')

       editappointment.save()
       messages.success(request, "Your appointment has been created")
       return redirect('/show')

   else:
       return render(request,'edit.html',{'editappointment':editappointment})

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('/home')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')
