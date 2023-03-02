from .models import Album
from .forms import AlbumForm
from django.shortcuts import render, render, redirect, get_object_or_404


def list_albums(request):
    albums = Album.objects.all()
    # goes to the database and gets all instances of the model Album (Django ORM) = a query
    return render(request, 'albums/index.html', {'albums': albums})


def add_album(request):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            # save and instance of album object
            album_form.save()
            return redirect('home')
    form = AlbumForm()
    return render(request, 'albums/add_album.html', {'form': form})


def detail_album(request, pk):
    album_description = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/detail_album.html', {"album_description": album_description})


def edit_album(request, pk):
    album_to_edit = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album_form = AlbumForm(request.POST, instance=album_to_edit)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    form = AlbumForm(instance=album_to_edit)
    return render(request, 'albums/edit_album.html', {'form': form})


def delete_album(request, pk):
    album_to_delete = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album_to_delete.delete()
        return redirect('home')
    return render(request, 'albums/delete_album.html')
