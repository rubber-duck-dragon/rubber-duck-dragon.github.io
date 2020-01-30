from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .permissions import IsOwnerOrReadOnly
from vocab.models import Word, List
from django.contrib.auth.models import User
from .serializers import WordSerializer, ListSerializer, UserSerializer
import requests
from django.shortcuts import render
from django.http import HttpResponse
from chop.hmm import Tokenizer as HMMTokenizer
from rest_framework.response import Response


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

    def tokenize(request):
    if request.method == 'POST' and 'parse_text' in request.POST:
        # tokenize the text
        txt = request.POST['input']
        from chop.mmseg import Tokenizer as MMSEGTokenizer

        frequency_list = {}
        high_frequency_list = {}
        stop_words = ['.', '"', "'", "`", "，", ",", "。", ":", ";", "?", "!", "(", ")", "*", "/", "@", "-", "_000_", "「", "」", "、"]
        
        MT = MMSEGTokenizer()
        tokenized = list(MT.cut(txt))

        for word in tokenized:
            if word in stop_words:
                pass
            elif word not in frequency_list:
                frequency_list[word] = 1
            elif word in frequency_list:
                frequency_list[word] += 1
        
        # get the most frequent words
        for key in frequency_list:
            if frequency_list[key] > 3:
                high_frequency_list[key] = frequency_list[key]

        list_of_tuples = sorted(high_frequency_list.items() , reverse=True, key=lambda x: x[1])

        new_list = []
        # lookup the words in the database
        for tuple in list_of_tuples:
            if Word.objects.all().filter(simplified = tuple[0]).exists():
                new_word = Word.objects.filter(simplified=tuple[0])
                context = {
                    'word': new_word
                }
                for word in new_word:
                    new_list.append(word)
                    
        print(new_list)

        # return HttpResponse(list_of_tuples)
        return render(request, 'vocab/list_view.html', context)
    else:
        return render(request, 'vocab/home_page.html')
    

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 