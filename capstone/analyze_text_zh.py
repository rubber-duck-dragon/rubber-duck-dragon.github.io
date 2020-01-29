import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize
import string
# nltk.download('punkt')

class Text:
    def __init__(self, file, name):
        f = open(file)
        punct = ['.', ',', '?', ':', ';', '/', '(', ')', '-', '--', '"', "'", '“', '”', '’', '!', "''", "``", "'s", '_', "n't", "'ll"]
        self.name = name
        self.text = f.read().lower()
        self.with_punct = word_tokenize(self.text)
        self.tokens = [token for token in self.with_punct if not token in punct]

    def freq_dist(self):
        tokens = self.tokens
        fdist = FreqDist(tokens)
        top_10 = fdist.most_common(10)
        word_list= []
        for word, count in top_10:
            word_list.append(word) 
        print(word_list)

    def tag_words(self):
        tagged = nltk.pos_tag(self.tokens)
        tag_fd = nltk.FreqDist(tag for (word, tag) in tagged)
        return tag_fd.most_common()
        

text1 = Text('sample.txt', "Sample")
text1.freq_dist()
