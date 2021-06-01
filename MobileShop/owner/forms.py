from .models import Brand,Product
from django import forms
from django.forms import ModelForm

class BrandForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields=["brand_name"]