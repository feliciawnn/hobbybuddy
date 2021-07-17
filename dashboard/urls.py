from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard')
]