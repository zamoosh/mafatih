
from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=150)
    type = models.PositiveSmallIntegerField()

class Singer(models.Model):
    name = models.CharField(max_length=100)

class Prayer(models.Model):
    tag = models.ManyToManyField(Tag)
    singer = models.ManyToManyField(Singer)
    pharase_count = models.IntegerField(default=0)
    name = models.CharField(max_length=200)

class File(models.Model):
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE)
    file = models.FileField(upload_to='')

class Phrase(models.Model):
    prayer = models.ForeignKey(Prayer,on_delete=models.CASCADE)
    text = models.TextField()
    order = models.CharField()
    type = models.PositiveSmallIntegerField()

class Translate(models.Model):
    phrase = models.ForeignKey(Phrase,on_delete=models.CASCADE)
    name = models.CharField(max_length=3)
    text = models.TextField()
