from .models import Brand,Product
from django import forms
from django.forms import ModelForm

class BrandCreateForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields=["brand_name"]

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"