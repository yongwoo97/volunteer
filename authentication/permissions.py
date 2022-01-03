from rest_framework import permissions

class IsOwnerOrNothing(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.username == request.user
