from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin' and request.user.is_active

class IsNormalUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'user' and request.user.is_active
