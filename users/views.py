from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import CustomUser
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de un usuario de acuerdo al ID mandado.
    list:
        Regresa la lista de usuario en la base de datos.
    create:
        Crea un usuario en la base de datos.
    delete:
        Elimina un usuario.
    update:
        Actualiza un libro.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.request.user is not IsAuthenticated and self.request.method == 'POST':
            permissions = [AllowAny]
        return [permission() for permission in permissions]
