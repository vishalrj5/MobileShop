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
from django.contrib import messages
from owner.models import Product,Cart
from owner.views import Get_Object
def indexx(request):
    return render(request,"index.html")




def Registration(request,*args,**kwargs):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, "Account created Successfully")
            return render(request,"CLogin.html")
        else:
            messages.error(request,"Registration Failed")
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
                return redirect("userhome")
            else:
                messages.error(request,"Invalid Username or Password")
                context["form"]=form
    return render(request,"CLogin.html",context)

def Sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


def User_Home(request,*args,**kwargs):
    mobiles=Product.objects.all()

    context={
        "mobiles":mobiles
    }
    return render(request,"homee.html",context)

def Item_Detail(request,*args,**kwargs):
    id=kwargs.get("id")
    mobile=Product.objects.get(id=id)
    context={
        "mobile":mobile
    }

    return render(request,"Product_Detail.html",context)

def add_to_cart(request,*args,**kwargs):
    pid=kwargs.get("id")
    product=Get_Object(pid)
    cart=Cart(product=product,user=request.user)
    cart.save()
    return redirect("userhome")

def my_cart(request,*args,**kwargs):
    cart_items=Cart.objects.filter(user=request.user,status="cart")
    context={
        "cart_items":cart_items

    }
    return render(request,"my_cart.html",context)

def remove_cart(request, *args,**kwargs):
    pid = kwargs.get("id")
    product = Get_Object(pid)
    product.delete()
    cart_items = Cart.objects.filter(user=request.user, status="cart")
    context = {
        "cart_items": cart_items

    }
    return render(request, "my_cart.html", context)

# Login page styling
# Remove item
# Orders product,(foreign key) user,address,status(ordered,packed,shipped,canceled,)