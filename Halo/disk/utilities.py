import os
import shutil


def get_link_create(path):
    try:
        return 'http://localhost:8000/disk/' + path
    except:
        return 'http://localhost:8000/disk/'


def get_link_delete(path):
    try:
        path = path[:-1].rpartition('/')[0]
        if path == '':
            return 'http://localhost:8000/disk/'
        else:
            return 'http://localhost:8000/disk/' + path + '/'
    except:
        return 'http://localhost:8000/disk/'


def create_user_file(user_id, path, name):
    f = open('media/' + user_id + '/' + path + name, 'wb')
    f.close()
    return True


def create_user_folder(user_id, path, name):
    return os.mkdir('media/' + user_id + '/' + path + '/' + name)


def delete_user_folder(user_id, path):
    # Рекурсивное удаление каталога и его содержимого
    return shutil.rmtree('media/' + user_id + path, ignore_errors=False, onerror=None)


def delete_user_file(user_id, path):
    return os.remove('media/' + user_id + path)


def get_user_folder_content(path):
    dirs = []
    files = []
    for element in os.listdir('media/' + path):
        if os.path.isdir('media/' + path + '/' + element):
            dirs.append(element)
        else:
            files.append(element)
    return [dirs, files]
