from django.urls import path,include
from .views import Registration,Sign_in,Sign_out
urlpatterns=[
    path("account",Registration,name="Reg"),
    path("signin",Sign_in,name="signin"),
    path("signout",Sign_out,name="signout"),
]