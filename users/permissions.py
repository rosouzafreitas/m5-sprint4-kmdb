from rest_framework import permissions



class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.user.is_superuser or request.user == obj and request.user.is_critic:
            return True
        
        return False
