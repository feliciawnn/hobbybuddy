from django.shortcuts import render, redirect
from .forms import NewActivityForm
from .models import Activity
from signup.models import UserActivity


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
    check = UserActivity.objects.filter(user=request.user, activity=act).count() > 0
    context = {
        'title': act.title,
        'picture': act.picture,
        'description': act.description,
        'cost': act.cost_estimation,
        'id': activity_id,
        'check': check,
    }
    return render(request, "activity/activitydetails.html", context)


def save_activity(request, activity_id):
    act = Activity.objects.get(pk=activity_id)
    sa = UserActivity(user=request.user, activity=act)
    sa.save()
    return redirect("/activity/" + str(activity_id))


def remove_activity(request, activity_id):
    act = Activity.objects.get(pk=activity_id)
    UserActivity.objects.filter(activity=act, user=request.user).delete()
    return redirect("/activity/" + str(activity_id))
