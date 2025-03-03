from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_category_list, name='photo_category_list'),
]