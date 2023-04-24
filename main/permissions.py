from rest_framework import permissions


class DeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE" and request.user.is_staff:
            return True
        return False
