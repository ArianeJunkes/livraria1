from rest_framework.viewsets import ModelViewSet

from livraria.models import Editora
from livraria.serializer import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer