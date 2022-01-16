from django.db import models
from django.utils.timezone import now


class Folder(models.Model):
    folder_name = models.CharField(unique=True,max_length=60)
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.folder_name

class Document(models.Model):
    name = models.CharField(unique=True,max_length=60)
    url = models.CharField(unique=False,max_length=255)
    folder_name = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=False)
    topics = models.ManyToManyField('Topic',related_name='documents',blank=False)
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.name



class Topic(models.Model):
    topics = models.CharField(max_length=50,unique=True)
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.topics

class File(models.Model):
    file = models.FileField()
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.file