from django.urls import path
from .views import Create_Brand,Delete_Brand,List_Brand,index
urlpatterns = [
    path('',index),
    path('brands',Create_Brand,name="createbrand"),
    path('listb',List_Brand,name="listbrand"),
    path('brands/remove/<int:id>',Delete_Brand,name="deletebrand")
]
