from django.shortcuts import render, redirect
from .forms import NewActivityForm
from .models import Activity


# Create your views here.
def create_activity(request):
    context = {}
    if request.method == "POST":
        form = NewActivityForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/dashboard")
        else:
            context['form'] = form
            return render(request, "activity/createactivity.html", context)

    context['form'] = NewActivityForm()
    return render(request, "activity/createactivity.html", context)


def activity_details(request, activity_id):
    act = Activity.objects.get(pk=activity_id)
    context = {
        'title': act.title,
        'picture': act.picture,
        'description': act.description,
        'cost': act.cost_estimation
    }
    return render(request, "activity/activitydetails.html", context)


