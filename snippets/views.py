#coding: utf-8
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import mixins
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