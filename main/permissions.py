from rest_framework import permissions


class DeletePermission(permissions.BasePermission):
    """
    Permission to allow staff members to perform DELETE requests.
    """

    def has_permission(self, request, view):
        if request.method == "DELETE":
            return request.user.is_staff
        return True
