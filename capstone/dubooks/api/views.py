from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .permissions import IsOwnerOrReadOnly
from .models import Word, List, User
from .serializers import WordSerializer, ListSerializer, UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'lists': reverse('list-detail', request=request, format=format),
        'words': reverse('word-detail', request=request, format=format),
        'users': reverse('user-detail', request=request, format=format),
    })

class WordView(viewsets.ReadOnlyModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class ListView(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 