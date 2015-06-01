from rest_framework import permissions

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        """ simply checking that the user of the request matches <account>
        """
        if request.user:
            return account == request.user
        return False
