from rest_framework import permissions


class IsAdminOrStockManager(permissions.BasePermission):
    """
    Custom permission to only allow admins or stock managers to manage stock data.
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD, or OPTIONS requests for any user
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is an admin or a stock manager
        return request.user and (
            request.user.is_staff
            or request.user.groups.filter(name="StockManager").exists()
        )
