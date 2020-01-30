from chop.hmm import Tokenizer as HMMTokenizer
import operator

# with open ("sample_book.txt") as file:
#     text = file.read()


frequency_list = {}
high_frequency_list = {}
stop_words = ['.', '"', "'", "`", "，", ",", "。", ":", ";", "?", "!", "(", ")", "*", "/", "@", "-", "_000_", "「", "」", "、"]

def main(txt):
    HT = HMMTokenizer()
    tokenized = list(HT.cut(txt))

    for word in tokenized:
        if word in stop_words:
            pass
        elif word not in frequency_list:
            frequency_list[word] = 1
        elif word in frequency_list:
            frequency_list[word] += 1
    
    for key in frequency_list:
        if frequency_list[key] > 3:
            high_frequency_list[key] = frequency_list[key]

    list_of_tuples = sorted(high_frequency_list.items() , reverse=True, key=lambda x: x[1])
 
    return list_of_tuples