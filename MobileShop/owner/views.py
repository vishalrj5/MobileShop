from django.shortcuts import render,redirect
from .forms import BrandForm
from .models import Brand
# Create your views here.
def index(request):
    return render(request,'index.html')

def Create_Brand(request):
    if request.method=="GET":
        form=BrandForm()
        context={}
        context["form"]=form
        return render(request,'createbrand.html',context)
    elif request.method=="POST":
        form=BrandForm(request.POST)
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
    form=BrandForm(instance=brand);
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BrandForm(instance=brand,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listbrand")
    return render(request,"editbrand.html",context)