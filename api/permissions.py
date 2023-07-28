from rest_framework import permissions

class IsAuthorOrReadyOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.profile_user == request.user

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner.profile_user == request.user

class isProfileOwnerOrReadyOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.profile_user == request.user

class haveNoProfileYet(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if hasattr(user, 'profile'):
            return False
        else:
            return True


