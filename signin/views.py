from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        signinform = forms.SignInForm(data=request.POST)
        if signinform.is_valid():
            signinform.save()
            return redirect("/dashboard")
        context['signinform'] = signinform
        return render(request, "signin/signin.html", context)
    else:
        context['signinform'] = forms.SignInForm()
    return render(request, "signin/signin.html", context)