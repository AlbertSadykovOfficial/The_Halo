from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse
from .utilities import get_files


def index(request):
    template = loader.get_template('music/index.html')
    files = get_files()
    """
    f = open(files[2], 'rb')
    urls = f.readlines()
    f.close()
    """
    return HttpResponse(template.render({'files': files}, request))