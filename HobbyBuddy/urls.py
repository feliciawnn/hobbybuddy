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

urlpatterns = [
    path('', welcome_view.index, name='welcome'),
    path('signup/', signup_view.index, name='signup'),
    path('dashboard/', dashboard_view.index, name='dashboard'),
    path('admin/', admin.site.urls),
]
