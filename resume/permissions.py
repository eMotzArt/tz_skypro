from rest_framework import permissions
from rest_framework.request import Request

from resume.models import Resume


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj: Resume) -> bool:
        if request.method != 'PATCH':
            return True
        return request.user == obj.author
