from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):
    """
    Custom permission to only allow sellers to create, update, or delete products.
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated and request.user.is_seller
