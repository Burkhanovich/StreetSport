from rest_framework import permissions


class IsAdminOrStadiumOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role==1:
            return True
        if obj.owner==request.user:
            return True
        return False












