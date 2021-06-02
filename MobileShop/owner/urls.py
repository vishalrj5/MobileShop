from django.urls import path
from .views import List_Product,Create_Product,Create_Brand,Delete_Brand,List_Brand,index,Edit_Brand
urlpatterns = [
    path('',index,name="index"),
    path('brands',Create_Brand,name="createbrand"),
    path('listb',List_Brand,name="listbrand"),
    path('brands/remove/<int:id>',Delete_Brand,name="deletebrand"),
    path('update/<int:id>',Edit_Brand,name="editbrand"),
    path('products',Create_Product,name="createproduct"),
    path("items",List_Product,name="items"),

]
