
from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=150)
    TAG_CHOICES = (('menu','MENU'),('date', 'DATE'))
    color = models.CharField(max_length=4, choices=TAG_CHOICES, default='date')

class Singer(models.Model):
    name = models.CharField(max_length=100)

class Prayer(models.Model):
    tag = models.ManyToManyField(Tag)
    singer = models.ManyToManyField(Singer)
    pharase_count = models.IntegerField(default=0)
    name = models.CharField(max_length=200)

class File(models.Model):
    relate = models.ForeignKey(Singer,name='relate',on_delete=models.CASCADE)
    file = models.FileField(upload_to='')

class Phrase(models.Model):
    Prayer_id = models.ForeignKey(Prayer,name='Prayer_id',on_delete=models.CASCADE)
    text = models.TextField(max_length=10000)
    order = models.IntegerField()
    type = models.IntegerField()

class Translate(models.Model):
    combine = models.ForeignKey(Phrase,name="combine",on_delete=models.CASCADE)
    name = models.CharField(max_length=2)
    text = models.TextField(max_length=10000)
