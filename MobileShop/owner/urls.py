from django.urls import path
from .views import Detail_Product,Detail_Product,Edit_Product,List_Product,Create_Product,Create_Brand,Delete_Brand,List_Brand,index,Edit_Brand
urlpatterns = [
    path('',index,name="index"),
    path('brands',Create_Brand,name="createbrand"),
    path('listb',List_Brand,name="listbrand"),
    path('brands/remove/<int:id>',Delete_Brand,name="deletebrand"),
    path('update/<int:id>',Edit_Brand,name="editbrand"),
    path('products',Create_Product,name="createproduct"),
    path("items",List_Product,name="items"),
    path("items/change/<int:id>",Edit_Product,name="change"),
    path("item/<int:id>",Detail_Product,name="productdetail"),
    path("item/remove/<int:id>",Detail_Product,name="productremove")

]
