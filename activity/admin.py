from django.contrib import admin
from .models import Activity, Category, UserCategory

# Register your models here.
admin.site.register(Activity)
admin.site.register(Category)
admin.site.register(UserCategory)