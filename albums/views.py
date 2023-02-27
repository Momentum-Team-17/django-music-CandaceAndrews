from django.shortcuts import render
from .models import Album


def list_albums(request):
    albums = Album.objects.all()
    # goes to the database and gets all instances of the model Album (Django ORM) = a query
    return render(request, 'albums/index.html', {'albums': albums})
