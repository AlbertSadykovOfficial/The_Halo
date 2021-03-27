import os
import pathlib

from django.shortcuts import redirect

from Halo import settings

from django.db import models

def get_files():
    fileDir = r"D:\WorkSpace\Programmng\The Halo\Halo\media"
    fileExt = r"**\*.mp3"
    audio_track = models.FileField(upload_to="media/3/Vicetone/vicetone-catch-me-original-mix.mp3")
    #filename = settings.MEDIA_URL + '/3/Vicetone/vicetone-catch-me-original-mix.mp3'
    #list(pathlib.Path(fileDir).glob(fileExt))
    return audio_track