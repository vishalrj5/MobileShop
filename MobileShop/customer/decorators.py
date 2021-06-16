from django.shortcuts import redirect
from owner.models import Cart


def loginrequired(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return func(request,*args,**kwargs)
    return wrapper


# def Permission_Required(func):
#     def wrapper(request,*args,**kwargs):
#         id=kwargs.get("id")
#         cart=Cart.objects.get(id=id)
#         print(cart.user)
#         print(request.user)
#