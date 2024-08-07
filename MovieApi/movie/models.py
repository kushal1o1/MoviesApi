from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.FloatField()
    cast = models.TextField()

    def __str__(self):
        return self.title