from django.contrib import admin
from .models import Task

"""
Добавление в админку управления моделью Task.
"""
admin.site.register(Task)

