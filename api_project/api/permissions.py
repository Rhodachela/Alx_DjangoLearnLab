from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admins to modify objects.
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD, or OPTIONS requests for everyone
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        # Allow write permissions only to admins
        return request.user and request.user.is_staff
