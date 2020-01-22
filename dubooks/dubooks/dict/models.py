from django.db import models

class DictEntry(models.Model):
    chinese_content = models.CharField(max_length=30)
    english_content = models.CharField(max_length=200)
    pinyin = models.CharField(max_lenth=50)
    part_of_speech= models.CharField(max_length=50)
    hsk_level = models.IntegerField()
    is_name = models.BooleanField()

    def __str__(self):
        return self.name


