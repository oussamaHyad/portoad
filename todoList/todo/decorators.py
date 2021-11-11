from django.http import HttpResponse
from django.shortcuts import redirect


" This Prevent a user to access a Login Page if He logged in"
def unauthenticated_user(view_func):
    def inside(request, *args , **kwargs):

        if request.user.is_authenticated:
            return redirect("home")

        else:
            return view_func(request, *args, **kwargs)            
            
    return inside




def clientOnly(view_func):
    def inside(request, *args , **kwargs):
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "client":
            return view_func(request , *args , **kwargs)

        else:
            return HttpResponse("Raise Error")

    return inside    


def onlyAdmin(view_func):
    def inside(request, *args , **kwargs):
        
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "admin":
            return view_func(request, *args , **kwargs)

    return inside