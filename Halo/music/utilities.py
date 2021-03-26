import os
import pathlib

def get_files():
    fileDir = r"D:\WorkSpace\Programmng\The Halo\Halo\media"
    fileExt = r"**\*.mp3"
    return list(pathlib.Path(fileDir).glob(fileExt))