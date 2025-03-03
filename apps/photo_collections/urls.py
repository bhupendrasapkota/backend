from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_collection_list, name='photo_collection_list'),
]