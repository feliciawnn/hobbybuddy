from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from . import forms


# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        signinform = forms.SignInForm(data=request.POST)
        if signinform.is_valid():
            user = signinform.get_user()
            login(request, user)
            return redirect("/dashboard")
        context['signinform'] = signinform
        return render(request, "signin/signin.html", context)
    else:
        context['signinform'] = forms.SignInForm()
    return render(request, "signin/signin.html", context)


def signout(response):
    logout(response)
    return redirect("/")