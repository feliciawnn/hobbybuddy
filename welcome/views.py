from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    return render(request, 'welcome/welcome.html')