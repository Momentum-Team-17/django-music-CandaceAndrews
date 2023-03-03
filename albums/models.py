from django.db import models


class Album(models.Model):
    # our model class is inheriting from Django's Model class located in models/
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'
