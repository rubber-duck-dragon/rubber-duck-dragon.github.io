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
    
class List(models.Model):
    name = models.CharField(max_length=100)
    words = models.ForeignKey(Word, on_delete=models.CASCADE)
    creator = models.CharField(max_length=100)

    def __str__(self):
        return self.name
 
class User(models.Model):
    username = models.CharField(max_length=50)
    lists = models.ForeignKey(List, on_delete=models.CASCADE)
    words = models.ManyToManyField(Word)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username