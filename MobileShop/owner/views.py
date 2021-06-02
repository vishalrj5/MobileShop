from django.shortcuts import render,redirect
from .forms import BrandCreateForm,ProductCreateForm
from .models import Brand,Product
# Create your views here.
def index(request):
    return render(request,'index.html')

def Create_Brand(request):
    if request.method=="GET":
        form=BrandCreateForm()
        context={}
        context["form"]=form
        return render(request,'createbrand.html',context)
    elif request.method=="POST":
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')

def List_Brand(request):
    form=Brand.objects.all()
    context={}
    context["form"]=form
    return render(request,'listbrand.html',context)


def Delete_Brand(request,id):
    form=Brand.objects.get(id=id);
    form.delete()
    return redirect('listbrand')

def Edit_Brand(request,id):
    brand=Brand.objects.get(id=id);
    form=BrandCreateForm(instance=brand);
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BrandCreateForm(instance=brand,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listbrand")
    return render(request,"editbrand.html",context)


# View for Creating and listing all products
# if the method is get this view will return all objects from models
# if method is post will create a new object inside models

def Create_Product(request):
    form=ProductCreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProductCreateForm(request.POST,files=request.FILES)
        if form.is_valid:
            form.save()
            return render(request,"product_create.html",context)
    return render(request,"product_create.html",context)

def List_Product(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"product_list.html",context)