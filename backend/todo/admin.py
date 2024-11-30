# todo/admin.py
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser 
from django.contrib import admin
from .models import Task # add this

class TodoAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description', 'completed') # add this

    # Register your models here.
admin.site.register(Task, TodoAdmin) # add this
admin.site.register(CustomUser,UserAdmin)