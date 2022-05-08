from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        # admin_permission = super().has_permission(request, view)
        admin_permission = bool(request.user and request.user.is_staff)

        # return request.method == 'GET' or admin_permission

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return admin_permission

class IsUserOrAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            # If the user is admin or the owner of the review
            # return obj.review_user == request.user or bool(request.user and request.user.is_staff)
            return obj.customer == request.user or request.user.is_staff

class IsUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            # If the user is admin or the owner of the review
            # return obj.review_user == request.user or bool(request.user and request.user.is_staff)
            return obj.customer == request.user