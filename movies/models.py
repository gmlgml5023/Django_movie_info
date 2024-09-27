from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    storyline = models.TextField()
    image = models.ImageField(blank=True)