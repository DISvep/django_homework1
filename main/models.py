from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)


class Game(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='games')
    release_year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)


