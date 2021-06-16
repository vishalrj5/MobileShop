from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ["first_name", "last_name","username","email","password1","password2"]
        widgets= {
            'first_name':forms.TextInput(attrs={'class':"form-control p-2"}),
            'last_name': forms.TextInput(attrs={'class': "form-control p-2"}),
            'username': forms.TextInput(attrs={'class': "form-control p-2"}),
            'email': forms.EmailInput(attrs={'class': "form-control p-2"}),
            'password1': forms.PasswordInput(attrs={'class': "form-control p-2"}),
            'password2': forms.PasswordInput(attrs={'class': "form-control p-2"})

        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': "form-control p-2"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control p-2"}))


class PlaceOrderForm(forms.Form):
    address=forms.CharField(widget=forms.Textarea)
    product=forms.CharField(max_length=120)
