from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        signupform = forms.SignUpForm(data=request.POST)
        if signupform.is_valid():
            signupform.save()
            return redirect("/signin")
        context['signupform'] = signupform
        return render(request, "signup/signuppage.html", context)
    else:
        context['signupform'] = forms.SignUpForm()
    return render(request, "signup/signuppage.html", context)


def profile_details(request):
    user = request.user
    context = {}
    context['first'] = user.first_name
    context['last'] = user.last_name
    context['email'] = user.email
    return render(request, 'signup/profiledetails.html', context)
