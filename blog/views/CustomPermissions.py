from rest_framework import permissions




class IsAdminOrModerator(permissions.BasePermission):
    """
    Custom permission to only allow admins or moderators to manage content.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.has_perm(
            f"blog.manage_{view.basename}"
        )


class IsAdminOrModeratorOrAuthor(permissions.BasePermission):
    """
    Custom permission to only allow admins, moderators, or comment authors to manage comments.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_staff
            or request.user.has_perm("blog.manage_comment")
            or obj.author == request.user
        )


class IsAuthenticatedClient(permissions.BasePermission):
    """
    Custom permission to only allow authenticated clients to like articles or comments.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.roles.filter(name="client").exists()
        )
