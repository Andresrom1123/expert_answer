from rest_framework import viewsets

from questions.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de una pregunta de acuerdo al ID mandado.
    list:
        Regresa la lista de preguntas en la base de datos.
    create:
        Crea una pregunta en la base de datos.
    delete:
        Elimina una pregunta.
    update:
        Actualiza una pregunta.
    """

    queryset = Question.objects.all()
    fields = '__all__'
