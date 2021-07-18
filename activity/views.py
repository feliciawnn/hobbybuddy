from django.shortcuts import render, redirect
from .forms import NewActivityForm, NewCategoryForm, CategoryChooser, ActivityCategoryForm
from .models import Activity, Category, UserCategory, ActivityCategory
from signup.models import UserActivity
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


# Create your views here.
@login_required(login_url="/")
def create_activity(request):
    if not request.user.is_staff:
        return redirect('/dashboard')
    context = {}
    categories = Category.objects.all()
    if request.method == "POST":
        form = NewActivityForm(data=request.POST, files=request.FILES)
        category_form = ActivityCategoryForm(data=request.POST, categories=categories)
        if form.is_valid() and category_form.is_valid():
            act = form.save()
            first = Category.objects.first().pk
            i = 0
            count = 0
            while count < len(category_form.cleaned_data):
                try:
                    cat = Category.objects.get(pk=i + first)
                    check = category_form.cleaned_data['cat%s' % count]
                    cc = ActivityCategory(activity=act, category=cat)
                    try:
                        if check:
                            cc.save()
                    except IntegrityError:
                        pass
                    count += 1
                except KeyError:
                    pass
                i += 1
            return redirect("/restricted/create-activity")
        else:
            context['form'] = form
            context['categorychoose'] = category_form
            return render(request, "activity/createactivity.html", context)

    context['form'] = NewActivityForm()
    context['categorychoose'] = ActivityCategoryForm(categories=categories)
    return render(request, "activity/createactivity.html", context)


@login_required(login_url="/")
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

    cat = ActivityCategory.objects.filter(activity=act)
    categories = []
    for category in cat:
        categories.append(category.category)
    context['categories'] = categories
    return render(request, "activity/activitydetails.html", context)


@login_required(login_url="/")
def save_activity(request, activity_id):
    act = Activity.objects.get(pk=activity_id)
    sa = UserActivity(user=request.user, activity=act)
    sa.save()
    return redirect("/activity/" + str(activity_id))


@login_required(login_url="/")
def remove_activity(request, activity_id):
    act = Activity.objects.get(pk=activity_id)
    UserActivity.objects.filter(activity=act, user=request.user).delete()
    return redirect("/activity/" + str(activity_id))


@login_required(login_url="/")
def saved_activity(request):
    saved = UserActivity.objects.filter(user=request.user)
    activities = []
    for ua in saved:
        act = Activity.objects.get(pk=ua.activity.pk)
        activities.append(act)
    context = {'acts': activities}
    return render(request, "activity/savedactivity.html", context)


@login_required(login_url="/")
def create_category(request):
    user = request.user
    if user.is_staff:
        if request.method == "POST":
            form = NewCategoryForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect("/restricted/create-category")
            return render(request, "activity/createcategory.html", {"form": form})
        return render(request, "activity/createcategory.html", {"form": NewCategoryForm()})
    else:
        return redirect("/dashboard")


@login_required(login_url="/")
def choose_category(request):
    categories = Category.objects.all()
    form = CategoryChooser(request.POST, categories=categories)

    if request.method == "POST":
        if form.is_valid():
            first = Category.objects.first().pk
            i = 0
            count = 0
            while count < len(form.cleaned_data):
                try:
                    cat = Category.objects.get(pk=i + first)
                    check = form.cleaned_data['cat%s' % count]
                    cc = UserCategory(user=request.user, category=cat)
                    try:
                        if check:
                            cc.save()
                        else:
                            search = UserCategory.objects.filter(user=request.user, category=cat)
                            if len(search) > 0:
                                search.delete()

                    except IntegrityError:
                        pass
                    count += 1
                except KeyError:
                    pass
                i += 1
        return redirect("/dashboard")
    return render(request, "activity/choosecategory.html", {"form": form})
