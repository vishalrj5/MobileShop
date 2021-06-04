from .models import Brand,Product
from django import forms
from django.forms import ModelForm

class BrandCreateForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields=["brand_name"]

class ProductCreateForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "specs": forms.Textarea(attrs={"class": "form-control"})
        }


    def clean(self):
        cleaned_data = super().clean()
        price=cleaned_data.get("price")
        if int(price)<500:

            msg = "invalid price"
            self.add_error("price",msg)