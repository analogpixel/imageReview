from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Create your models here.
class Image(models.Model):
    file_name = models.CharField(max_length=255) 
    tags      = models.ManyToManyField(Tag, related_name='items')
    stared    = models.BooleanField(default=False)
    notes     = models.TextField(default="")

    def __str__(self):
        return self.file_name



