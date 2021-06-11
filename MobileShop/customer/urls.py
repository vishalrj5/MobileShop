from django.urls import path,include
from .views import remove_cart,my_cart,add_to_cart,Registration,Sign_in,Sign_out,indexx,User_Home,Item_Detail
urlpatterns=[
    path("",indexx,name="indx"),
    path("account",Registration,name="Reg"),
    path("signin",Sign_in,name="signin"),
    path("signout",Sign_out,name="signout"),
    path("hom",User_Home,name="userhome"),
    path("detail/<int:id>",Item_Detail,name="itemdetail"),
    path("carts",my_cart,name="my_cart"),
    path("cart/<int:id>",add_to_cart,name="add_to_cart"),
    path("removed",remove_cart,name="removes")
]