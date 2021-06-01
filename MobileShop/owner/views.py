from django.shortcuts import render
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


def Delete_Brand(request):
    pass