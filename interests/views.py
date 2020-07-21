from rest_framework import viewsets

from interests.models import Interest
from interests.serializers import InterestSerializer


class InterestViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de un interés de acuerdo al ID mandado.
    list:
        Regresa la lista de intereses en la base de datos.
    create:
        Crea un interés en la base de datos.
    delete:
        Elimina un interés.
    update:
        Actualiza un interés.
    """

    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
