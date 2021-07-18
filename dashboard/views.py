from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from activity.models import Activity, ActivityCategory, UserCategory


# Create your views here.
@login_required(login_url="/")
def index(request):
    context = {'first': request.user.first_name, 'last': request.user.last_name}
    user_category = UserCategory.objects.filter(user=request.user)
    preferred_category = []
    for uc in user_category:
        preferred_category.append(uc.category)

    preferred_activity = ActivityCategory.objects.filter(category__in=preferred_category)
    activities = []
    for pa in preferred_activity:
        activities.append(pa.activity)
    context['activities'] = activities
    return render(request, "dashboard/dashboard.html", context)


@login_required(login_url="/")
def search_index(request, keyword):
    context = {'first': request.user.first_name, 'last': request.user.last_name}
    context['activities'] = Activity.objects.filter(title__contains=keyword)
    return render(request, "dashboard/dashboard.html", context)


def search_redirect(request):
    keyword = request.GET.get('search')
    return redirect('/dashboard/' + keyword)