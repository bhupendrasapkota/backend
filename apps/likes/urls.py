from django.urls import path
from . import views

urlpatterns = [
    path('', views.like_list, name='like_list'),
]