#coding: utf-8
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

class SnippetList(generics.ListCreateAPIView):
    """
    Listar todos os snippets
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retorna, modifica ou deleta uma instancia de snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer