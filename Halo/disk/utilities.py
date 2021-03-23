import os

# Рекурсивное удаление каталога и его содержимого
import shutil


def create_user_folder(id):
    return os.mkdir('media/' + id)


def delete_user_folder(id):
    return shutil.rmtree('media/' + id, ignore_errors=False, onerror=None)


def get_user_folder_content(id):
    dirs = []
    files = []
    for element in os.listdir('media/'+id):
        if os.path.isdir('media/' + id +'/'+ element):
            dirs.append(element)
        else:
            files.append(element)
    return [dirs, files]
