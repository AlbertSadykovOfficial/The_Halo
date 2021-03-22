from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm
import os

def index(request):
    template = loader.get_template('disk/index.html')
    folder = os.listdir()
    context = {'text': "тут файлики:", "folders": folder }
    return HttpResponse(template.render(context, request))

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = Img()
            file.img = form.cleaned_data['img']
            file.desc = form.cleaned_data['desc']
            file.save()
            # file is saved
            #form.save()
            return HttpResponseRedirect('')
    else:
        form = UploadFileForm()
    return render(request, 'disk/upload.html', {'form': form })