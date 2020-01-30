from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    traditional = models.CharField(max_length=30)
    simplified = models.CharField(max_length=30) 
    english = models.CharField(max_length=200)
    pinyin = models.CharField(max_length=50)
    hsk = models.IntegerField()

    def __str__(self):
        return self.simplified
    
class List(models.Model):
    name = models.CharField(max_length=100)
    words = models.ManyToManyField(Word, related_name="lists")
    creator = models.ForeignKey(User, related_name="lists", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
 
