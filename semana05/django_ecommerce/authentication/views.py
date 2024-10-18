from rest_framework import generics, status
from authentication.models import RoleModel, UserModel
from .serializers import RoleSerializer, UserSerializer, LoginSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework.serializers import ValidationError
from .permissions import (
    IsAuthenticated,
    IsAdmin,
    IsSeller,
    IsSellerOrAdmin,
)


class CreateRoleView(generics.CreateAPIView):
    serializer_class = RoleSerializer

    @swagger_auto_schema(tags=['Roles'])
    def post(self, request):
        """ Crea un rol (método POST) """
        response = super().post(request)

        return Response({
            'message': 'Role creado exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

class ListRoleView(generics.ListAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    @swagger_auto_schema(tags=['Roles'])
    def get(self, request):
        """ Listar roles (método GET) """
        response = super().get(request)

        return Response({
            'message': 'Roles listados exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)
    

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    @swagger_auto_schema(tags=['Usuarios'])
    def post(self, request):
        """ Crea un usuario (método POST) """
        response = super().post(request)

        return Response({
            'message': 'Usuario creado exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class UpdateUserView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(tags=['Usuarios'])
    def put(self, request, *args, **kwargs):
        """" Actualiza un usuario (método PUT) """
        response = super().put(request, *args, **kwargs)

        return Response({
            'message': 'Usuario actualizado exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(tags=['Usuarios'])
    def patch(self, request, *args, **kwargs):
        """ Actualiza parcialmente un usuario (método PATCH) """
        response = super().partial_update(request, *args, **kwargs)

        return Response({
            'message': 'Usuario actualizado exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)

class ListUserView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(tags=['Usuarios'])
    def get(self, request, *args, **kwargs):
        """ Listar usuarios (método GET) """
        response = super().get(request, *args, **kwargs)

        return Response({
            'message': 'Usuarios listados exitosamente',
            'data': response.data
        }, status=status.HTTP_200_OK)
    

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ValidationError as e:
            return Response({
                'message': 'Credenciales incorrectas',
            }, status=status.HTTP_401_UNAUTHORIZED)