from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm

# Получить содержимое диска
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist

# Загрузка файлов в определенный каталог
from django.core.files.storage import FileSystemStorage

# Регистрация
from .models import DiskUser
from .forms import RegisterUserForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

# Удаление пользователя:
from django.views.generic.edit import DeleteView
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404

# Для старницы входа
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Для старницы выхода (дполнительно)
# Чтобы страица была доступна только зарегистрированным пользователям
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# Дополниельные приложения
from .utilities import delete_user_folder
from .utilities import get_user_folder_content


@login_required
def index(request):
    template = loader.get_template('disk/index.html')
    user_id = str(request.user.id)
    objects = get_user_folder_content(user_id)
    context = {'text': "тут файлики:", "folders": objects[0], "files": objects[1]}
    return HttpResponse(template.render(context, request))

@login_required
def other_page(request, folder):
    print(request.path[6:])
    try:
        # К полученному имени выводимой страницы (page)
        # Добавляем расшиерение и префикс каталога
        template = loader.get_template('disk/index.html')
        user_id = str(request.user.id)
        objects = get_user_folder_content(user_id +'/'+ folder)
        context = {'text': "тут файлики:", "folders": objects[0], "files": objects[1]}
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(context, request))


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            user_id = str(request.user.id)
            folder = 'media/' + user_id
            # Устанавливаем путь для сохранения
            fs = FileSystemStorage(location=folder)
            fs.save(request.FILES['file'].name, request.FILES['file'])

            # form.save()
            return HttpResponseRedirect('http://localhost:8000/disk/')
    else:
        form = UploadFileForm()
    return render(request, 'disk/upload.html', {'form': form})


# Контроллер регистрирующий пользователя
class RegisterUserView(CreateView):
    model = DiskUser
    template_name = 'disk/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('disk:register_done')


# Контроллер, выводящий сообщение об успшной регистрации
class RegisterDoneView(TemplateView):
    template_name = 'disk/register_done.html'


# Страница входа
# В файле проекта установлен редирект на приложение disk
# LOGIN_REDIRECT_URL = '/disk/'
class DiskLoginView(LoginView):
    template_name = 'disk/login.html'


# Страница выхода
# Нужно, чтобы она была доступна только зарегистрированным пользователям
# Для этого добавляем класс LoginRequiredMixin
class DiskLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'disk/logout.html'


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = DiskUser
    template_name = 'disk/delete_user.html'
    success_url = reverse_lazy('disk:index')

    # Сохраняем ключ пользователя
    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    # Выполнить выход перед удалением
    # После выполнения выхода сообщение пропадает
    # Поэтому мы создаем это сообщение самостоятельно
    def post(self, request, *args, **kwargs):
        user_id = str(request.user.id)
        delete_user_folder(user_id)
        logout(request)
        # messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
        return super().post(request, *args, **kwargs)

    # Извлечение удаляемой записи выполняется в get_object(),
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


""" 

def upload(request):
    folder='my_folder/'
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT
        filename = fs.save(myfile.name, myfile)
        file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'file_url': file_url
        })
    else:
         return render(request, 'upload.html')
"""
