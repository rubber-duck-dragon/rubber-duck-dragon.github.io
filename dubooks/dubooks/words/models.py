from django.db import models

# Create your models here.
class Word(models.Model):
    traditional = models.CharField(max_length=30)
    simplified = models.CharField(max_length=30) 
    english = models.CharField(max_length=200)
    pinyin = models.CharField(max_length=50)
    hsk = models.IntegerField()
    

    def __str__(self):
        return self.simplified