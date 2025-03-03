from django.urls import path
from . import views

urlpatterns = [
    path('', views.follower_list, name='follower_list'),
]