from rest_framework import permissions


class IsAdminOrStockManager(permissions.BasePermission):
    """
    Custom permission to only allow admins or stock managers to manage stock data.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        retur
