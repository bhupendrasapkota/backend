from django.urls import path, include
from apps.authentication.views import AuthenticationViewSet, LogoutView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'auth', AuthenticationViewSet, basename='authentication')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
