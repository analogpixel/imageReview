from django.db import models

# images for this day
class Day(models.Model):
    id   = models.AutoField(primary_key=True)
    date = models.DateField(unique=True)
    images = models.ManyToManyField('Image', related_name='days')

    def __str__(self):
        return str(self.date)

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



