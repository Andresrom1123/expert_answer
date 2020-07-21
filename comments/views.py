from rest_framework import viewsets

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de un comentario de acuerdo al ID mandado.
    list:
        Regresa la lista de comentarios en la base de datos.
    create:
        Crea un comentario en la base de datos.
    delete:
        Elimina un comentario.
    update:
        Actualiza un comentario.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
