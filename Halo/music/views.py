import os

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import MediaModel
from .models import MediaForm
from Halo.settings import MEDIA_URL


"""
# files = get_files()
f = open(files[2], 'rb')
urls = f.readlines()
f.close()
# import os
# print(os.path.abspath(song.media_file.url))
# context = {'song': song, 'name': os.path.basename(song.media_file.name)}
"""

def index(request):
    template = loader.get_template('music/index.html')
    song = MediaModel.objects.get(pk=1).media_file.name
    song_url = MEDIA_URL + song
    context = {'name': os.path.basename(song), 'song_url': song_url}
    return HttpResponse(template.render(context, request))



def media_create(request):
    template = loader.get_template('music/create.html')
    if request.method == "POST":
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://localhost:8000/music/')
    else:
        form = MediaForm()
    return HttpResponse(template.render({'form': form}, request))
