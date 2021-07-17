from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        signupform = forms.SignUpForm(data=request.POST)
        if signupform.is_valid():
            signupform.save()
            return redirect("/dashboard")
        context['signupform'] = signupform
        return render(request, "signup/signuppage.html", context)
    else:
        context['signupform'] = forms.SignUpForm()
    return render(request, "signup/signuppage.html", context)

