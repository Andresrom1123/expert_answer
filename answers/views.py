from rest_framework import viewsets

from answers.models import Answer
from answers.serializers import AnswerSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de una respuesta de acuerdo al ID mandado.
    list:
        Regresa la lista de respuestas en la base de datos.
    create:
        Crea una respuesta en la base de datos.
    delete:
        Elimina una respuesta.
    update:
        Actualiza una respuesta.
    """

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
