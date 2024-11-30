from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import TaskSerializer      # add this
from .models import Task                     # add this

class TaskView(viewsets.ModelViewSet):       # add this
    serializer_class = TaskSerializer          # add this
    queryset = Task.objects.all()              # add this