from django.shortcuts import render
from rest_framework import viewsets
from .models import Word
from .serializers import WordSerializer

class WordView(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
