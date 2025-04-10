from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 1

class IsAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 1 or request.user.role == 2


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 1 or request.user.role == 2 or request.user.role == 3

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role==2

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role==4







