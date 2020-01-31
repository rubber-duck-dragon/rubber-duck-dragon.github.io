import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from chop.hmm import Tokenizer as HMMTokenizer
from .models import List, Word
import json



def tokenize(request):

        # tokenize the text
    

    if request.method == 'POST':
        # txt = request.POST['input']
        json.loads(request.body)
        print("*"*100)
        from chop.mmseg import Tokenizer as MMSEGTokenizer
        txt = json.loads(request.body)["input_text"]
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
                if len(new_word) > 1:
                    print("duplicate!")
                for word in new_word:
                    new_list.append({
                        "simplified": word.simplified,
                        "traditional": word.traditional,
                        "pinyin": word.pinyin,
                        "english": word.english,
                        "hsk": word.hsk
                    })
               
        
            

        return JsonResponse({"data": new_list})
        
        # return render(request, 'vocab/list_view.html', context)
    else:
        return render(request, 'vocab/home_page.html')