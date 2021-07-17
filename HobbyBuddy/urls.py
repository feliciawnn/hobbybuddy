"""HobbyBuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from welcome import views as welcome_view
from signup import views as signup_view
from dashboard import views as dashboard_view
from signin import views as signin_view
from activity import views as activity_view

urlpatterns = [
    path('', welcome_view.index, name='welcome'),
    path('signup/', signup_view.index, name='signup'),
    path('signin/', signin_view.index, name='signin'),
    path('dashboard/', dashboard_view.index, name='dashboard'),
    path('create-activity/', activity_view.create_activity, name='create-activity'),
    path('activity/<int:activity_id>/', activity_view.activity_details, name='activity-details'),
    path('admin/', admin.site.urls),
]
