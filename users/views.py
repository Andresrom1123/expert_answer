from rest_framework import viewsets

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
