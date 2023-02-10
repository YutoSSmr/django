from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index_template, name='index_template'),
    path('words/', views.words, name='words'),
]