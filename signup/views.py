from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import forms


# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        signupform = forms.SignUpForm(data=request.POST)
        if signupform.is_valid():
            signupform.save()
            user = authenticate(username=signupform.cleaned_data['username'],
                                password=signupform.cleaned_data['password1'])
            login(request, user)
            return redirect("/choose-category")
        context['signupform'] = signupform
        return render(request, "signup/signuppage.html", context)
    else:
        context['signupform'] = forms.SignUpForm()
    return render(request, "signup/signuppage.html", context)


@login_required(login_url="/")
def profile_details(request):
    user = request.user
    context = {}
    context['first'] = user.first_name
    context['last'] = user.last_name
    context['email'] = user.email
    return render(request, 'signup/profiledetails.html', context)
