from rest_framework import generics, status
from authentication.models import RoleModel
from .serializers import RoleSerializer, UserSerializer
from rest_framework.response import Response


class CreateRoleView(generics.CreateAPIView):
    serializer_class = RoleSerializer

    def create(self, request):
        response = super().create(request)

        return Response({
            'message': 'Role creado exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)


class ListRoleView(generics.ListAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def list(self, request):
        response = super().list(request)

        return Response({
            'message': 'Roles listados exitosamente',
            'data': response.data
        })
    

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request):
        response = super().create(request)

        return Response({
            'message': 'Usuario creado exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)