from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from .models import MediaForm
from .utilities import get_context
from .utilities import change_music_meta


# Основаная страница
def index(request):
    template = loader.get_template('music/index.html')
    artist, title, album, time, song_url = get_context()
    form = MediaForm()
    context = {'artist': artist,
               'title': title,
               'album': album,
               'time': time,
               'song_url': song_url,
               'form': form
               }
    return HttpResponse(template.render(context, request))


# Загрузка файла на сервер
def media_create(request):
    template = loader.get_template('music/create.html')
    if request.method == "POST":
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Редактируем информацию трека по данным формы
            change_music_meta(request.POST['artist'],
                              request.POST['song'],
                              request.POST['album'],
                              request.FILES['media_file'].name
                              )
            return HttpResponseRedirect('http://localhost:8000/music/')
    else:
        form = MediaForm()
    return HttpResponse(template.render({'form': form}, request))
