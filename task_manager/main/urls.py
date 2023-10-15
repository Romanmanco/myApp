from django.urls import path
from . import views

"""
Настройки страниц, которые представлены в проекте.
"""

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create')
]