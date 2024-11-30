"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from todo import views                            # add this

router = routers.DefaultRouter()                      # add this
router.register(r'todos', views.TaskView, 'todo')     # add this

urlpatterns = [
    path('admin/', admin.site.urls),                        # add this
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_auth.urls')), path('api/auth/registration/', include('rest_auth.registration.urls')), path('accounts/', include('allauth.urls')),
    ]
