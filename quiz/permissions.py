from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow authors of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True
        
        try:
            return obj.quiz.author == request.user
        except AttributeError:
            try:
                return obj.question.quiz.author == request.user
            except AttributeError:
                pass

        # Write permissions are only allowed to the author of the object.
        return obj.author == request.user