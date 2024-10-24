from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed


def is_authenticated(request):
    if not request.user.is_authenticated:
        raise AuthenticationFailed(detail={
            'message': 'Credenciales incorrectas'
        }, code=401)
    
def is_role(request, role, message):
    if not request.user.role.name == role:
        raise AuthenticationFailed(detail={
            'message': f'No tiene permisos de {message}'
        }, code=401)

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        is_authenticated(request)
        return True
    
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        is_authenticated(request)
        is_role(request, 'ADMIN', 'administrador')
        return True
    
class IsSeller(BasePermission):
    def has_permission(self, request, view):
        is_authenticated(request)
        is_role(request, 'SELLER', 'vendedor')
        return True
    
class IsSellerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        is_authenticated(request)

        role = request.user.role.name
        if role == 'ADMIN' or role == 'SELLER':
            return True
        
        raise AuthenticationFailed(detail={
            'message': 'No tiene permisos de usuario'
        }, code=401)