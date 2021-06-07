from django.shortcuts import render,redirect

# Create your views here.
# Register your views
# Login
# Logout
# auth



# ViewProducts

# Add to cart

# placeorder

# manageorders
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login as djangologin,logout

def Registration(request,*args,**kwargs):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"CLogin.html")
        else:
            context["form"]=form

    return render(request,"CRegistration.html",context)

def Sign_in(request,*args,**kwargs):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                djangologin(request,user)
                return render(request,"Home.html")

    return render(request,"CLogin.html",context)

def Sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")
