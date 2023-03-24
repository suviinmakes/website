from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

def register(request):
    if request.method =='POST':
        username= request.POST['username']
        email= request.POST['email']
        firstname= request.POST['first_name']
        lastname= request.POST['last_name']
        password= request.POST['password']
        cpassword= request.POST['confirm_password']
        if password==cpassword:
            res= User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)
            res.save();
            print("user created")
        else:
            print("password not matching")
    return render(request,"register.html")
