import math
import eyed3

from random import randint, random
from django.db.models import Max
from Halo.settings import MEDIA_URL

from .models import MediaModel


# Получить продолжительность проигрывания
def duration_from_seconds(s):
    s = s
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    timelapsed = "{:01d}:{:02d}".format(int(m), int(s))
    return timelapsed


# Получить Модель по рандомному id
# Странновато работает, но работает
def get_random_item(model, max_id=None):
    if max_id is None:
        max_id = list(model.objects.aggregate(Max('id')).values())[0]
    min_id = math.ceil(max_id * random())
    return model.objects.filter(id__gte=min_id)[0]


# Получить параметры для вывода информации трека
def get_context():
    song = get_random_item(MediaModel).media_file.name
    song_url = MEDIA_URL + song
    song_tags = eyed3.load('media/' + song)
    time = duration_from_seconds(song_tags.info.time_secs)
    return [song_tags.tag.artist, song_tags.tag.title, song_tags.tag.album, time, song_url]


# Редактируем информацию трека по данным формы
#
# Django при сохранении изменяет некоторые имена файлов
# К примеру, если в названии есть пробелы, запрещенные симолы
# или если файл с таким имененм уже существовал
#
# Поэтому до файла по его изначальному имени не
# будет возмоности достучаться -> будет Ошибка открытия
# Обраьатываем ее и забиваем на редактирование
def change_music_meta(artist, song, album, filename):
    try:
        song_tags = eyed3.load('media/music/songs/' + artist + '/' + album + '/' + filename.replace(' ', '_'))
        song_tags.tag.artist = artist
        song_tags.tag.title = song
        song_tags.tag.album = album
        # Переименовать
        song_tags.rename(artist + ' - ' + song)
        # song_tags.tag.save()
    except:
        pass
