from django.db import models
from django.forms.models import modelform_factory


# Получаем путь для загрузки файла
# Если при загрузке файла не были
# введены данные Исполнителя и Альбома,
# то они устанавливаются в значение other
def get_upload_to(instance, filename):
    if instance.artist == '':
        artist = 'other'
    else:
        artist = instance.artist

    if instance.album == '':
        album = 'other'
    else:
        album = instance.album

    return 'music/songs/%s/%s/%s' % (artist, album, filename)


class MediaModel(models.Model):
    artist = models.CharField(blank=True, default=None, max_length=40, verbose_name='Исполнитель')
    album = models.CharField(blank=True, default=None, max_length=40, verbose_name='Альбом')
    song = models.CharField(blank=True, default=None, max_length=100, verbose_name='Композиция')
    media_file = models.FileField(upload_to=get_upload_to)


MediaForm = modelform_factory(MediaModel, fields={'artist', 'album', 'song', 'media_file'})
