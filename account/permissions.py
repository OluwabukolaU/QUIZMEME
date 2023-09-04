from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):
    def permitted(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id==request.user.id