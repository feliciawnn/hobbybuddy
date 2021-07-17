from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from activity.models import Activity


# Create your views here.
@login_required(login_url="/signin")
def index(request):
    context = {}
    context['first'] = request.user.first_name
    context['last'] = request.user.last_name
    context['activities'] = Activity.objects.all()
    return render(request, "dashboard/dashboard.html", context)