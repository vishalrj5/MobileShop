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
from .forms import UserRegistrationForm,LoginForm,PlaceOrderForm
from django.contrib.auth import authenticate,login as djangologin,logout
from django.contrib import messages
from owner.models import Product,Cart,Orders
from owner.views import Get_Object
from .decorators import loginrequired
from django.db.models import Sum

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

@loginrequired
def User_Home(request,*args,**kwargs):
    mobiles=Product.objects.all()
    cnt=Cart.objects.filter(user=request.user,status='cart').count()
    print(cnt)
    context={
        "cnt":cnt,
        "mobiles":mobiles
    }
    return render(request,"homee.html",context)

@loginrequired
def Item_Detail(request,*args,**kwargs):
    id=kwargs.get("id")
    mobile=Product.objects.get(id=id)
    context={
        "mobile":mobile
    }

    return render(request,"Product_Detail.html",context)

@loginrequired
def add_to_cart(request,*args,**kwargs):
    pid=kwargs.get("id")
    product=Get_Object(pid)
    cart=Cart(product=product,user=request.user)
    cart.save()
    return redirect("userhome")

@loginrequired
def my_cart(request,*args,**kwargs):
    cart_items=Cart.objects.filter(user=request.user,status="cart")
    total = Cart.objects.filter(status='cart', user=request.user).aggregate(Sum('product__price'))

    context={
        "cart_items":cart_items,
        "total":total

    }

    return render(request,"my_cart.html",context)

@loginrequired
def remove_cart(request,*args,**kwargs):
    pid = kwargs.get("id")
    productrem = Cart.objects.get(id=pid)
    productrem.delete()
    return redirect("my_cart")

# Login page styling
# Remove item
# Orders product,(foreign key) user,address,status(ordered,packed,shipped,canceled,)

@loginrequired
def place_order(request,*args,**kwargs):
    pid=kwargs.get("id")
    print("Cart Id", kwargs)
    mobile=Get_Object(pid)
    context={
        "form":PlaceOrderForm(initial={"product":mobile.mobile_name})
    }
    if request.method == "POST":
        cid=kwargs.get("cid")
        cartobj=Cart.objects.get(id=cid)
        form=PlaceOrderForm(request.POST)
        if form.is_valid():
            address=form.cleaned_data["address"]
            order=Orders(address=address,product=mobile,user=request.user)
            order.save()
            cartobj.status="orderplaced"
            cartobj.save()
            return redirect("userhome")

    return render(request,"PlaceOrders.html",context)


def List_Order(request,*args,**kwargs):
    order_items = Orders.objects.filter(user=request.user)
    context = {
        "order_items": order_items

    }
    return render(request,"ListOrders.html",context)

# def Cancel_Order(request,*args,**kwargs):
#