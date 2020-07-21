from rest_framework import viewsets

from topics.models import Topic
from topics.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de un tema de acuerdo al ID mandado.
    list:
        Regresa la lista de temas en la base de datos.
    create:
        Crea un tema en la base de datos.
    delete:
        Elimina un tema.
    update:
        Actualiza un tema.
    """

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
