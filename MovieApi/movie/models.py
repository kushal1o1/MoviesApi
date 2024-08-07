from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.TextField()
    cast = models.TextField()
    language = models.TextField()
    isbn = models.TextField()
    rating =models.FloatField()
    director =models.TextField()

    def __str__(self):
        return self.title