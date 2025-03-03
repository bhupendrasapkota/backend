from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories/', include('apps.categories.urls')),
    path('api/collections/', include('apps.collection.urls')),
    path('api/comments/', include('apps.comments.urls')),
    path('api/downloads/', include('apps.downloads.urls')),
    path('api/followers/', include('apps.followers.urls')),
    path('api/likes/', include('apps.likes.urls')),
    path('api/photo_categories/', include('apps.photo_categories.urls')),
    path('api/photo_collections/', include('apps.photo_collections.urls')),
    path('api/photos/', include('apps.photos.urls')),
    path('api/users/', include('apps.users.urls')),
]