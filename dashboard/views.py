from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/signin")
def index(request):
    context = {}
    context['first'] = request.user.first_name
    context['last'] = request.user.last_name
    return render(request, "dashboard/dashboard.html", context)