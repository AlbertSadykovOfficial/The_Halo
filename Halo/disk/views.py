from django.core.files import File

from django.shortcuts import render
from django.template import loader

# Получить содержимое диска
from django.http import HttpResponse, HttpResponseRedirect, Http404
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

# Изменение пароя
from django.contrib.auth.views import PasswordChangeView

# Изменение личной информации
from django.views.generic.edit import UpdateView
from .forms import ChangeUserInfoForm

# Дополниельные приложения
from .utilities import rename
from .utilities import folder_archive
from .utilities import get_link_create
from .utilities import get_link_delete
from .utilities import create_user_file
from .utilities import delete_user_file
from .utilities import create_user_folder
from .utilities import delete_user_folder
from .utilities import get_user_folder_content


@login_required
def index(request):
    template = loader.get_template('disk/index.html')
    # Получаем каталог пользователя по его ID
    user_id = str(request.user.id)
    objects = get_user_folder_content(user_id)

    context = {
        'path': "",
        'folders': objects[0],
        'files': objects[1],
    }
    return HttpResponse(template.render(context, request))


@login_required
def other_page(request, folder):
    try:
        template = loader.get_template('disk/index.html')

        # Получаем каталог пользователя по его ID
        user_id = str(request.user.id)
        objects = get_user_folder_content(user_id + '/' + folder)

        context = {
            'path': folder,
            'folders': objects[0],
            'files': objects[1],
        }
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(context, request))


@login_required
def upload_files(request, path):
    redirect = get_link_create(path)
    user_id = str(request.user.id)
    folder = 'media/' + user_id + '/' + path

    # Устанавливаем путь для сохранения
    fs = FileSystemStorage(location=folder)
    fs.save(request.FILES['file'].name, request.FILES['file'])

    return HttpResponseRedirect(redirect)


@login_required
def create_file(request, path):
    redirect = get_link_create(path)
    user_id = str(request.user.id)
    name = request.POST['new_name']
    create_user_file(user_id, path, name)
    return HttpResponseRedirect(redirect)


@login_required
def create_folder(request, path):
    redirect = get_link_create(path)
    user_id = str(request.user.id)
    name = request.POST['new_name']
    create_user_folder(user_id, path, name)
    return HttpResponseRedirect(redirect)


@login_required
def delete_file(request, path):
    redirect = get_link_delete(path)
    user_id = str(request.user.id)
    delete_user_file(user_id, '/' + path[:-1])
    return HttpResponseRedirect(redirect)


@login_required
def delete_folder(request, path):
    redirect = get_link_delete(path)
    user_id = str(request.user.id)
    delete_user_folder(user_id, '/' + path)
    return HttpResponseRedirect(redirect)


def change_name(request, path):
    redirect = get_link_create(path)
    if path == '':
        path = path + '/'
    user_id = str(request.user.id)
    old_name = request.POST['old_name']
    new_name = request.POST['new_name']
    rename(user_id + '/' + path, old_name, new_name)
    return HttpResponseRedirect(redirect)


def download_file(request, path):
    user_id = str(request.user.id)
    folder = 'media/' + user_id + '/' + path
    f = open(folder, 'rb')
    myfile = File(f)
    response = HttpResponse(myfile)
    response['Content-Disposition'] = 'attachment;'
    return response


# СДЕЛАТЬ
def download_folder(request, path):
    user_id = str(request.user.id)
    myfile = folder_archive(user_id, path)
    response = HttpResponse(myfile)
    response['Content-Disposition'] = 'attachment;'
    return response


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
        delete_user_folder(user_id, '')
        logout(request)
        # messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
        return super().post(request, *args, **kwargs)

    # Извлечение удаляемой записи выполняется в get_object(),
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class DiskPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'disk/password_change.html'
    success_url = reverse_lazy('disk:index')


# LoginRequiredMixin запрещает доступ к контроллеру готсям
# SuccessMessageMixin - вывод вслывающих сообщений об успешном выполнении операции
class ChangeUserInfoView(LoginRequiredMixin, UpdateView):
    model = DiskUser
    form_class = ChangeUserInfoForm
    template_name = 'disk/change_user_info.html'
    success_url = reverse_lazy('disk:index')

    # В процессе работы контроллер должен извлечь запись из модели AdvUser,
    # представляющую текущего пользователя,
    # для чего нужно получить ключ текущего пользователя (user.pk)
    #
    # Метод dispatch исполняется в САМОМ НАЧАЛЕ работы контроллера-класса,
    # поэтому это лучшее место для получения ключа
    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    # Извлечение исправляемой записи выполняется в get_object(),
    # которую конроллер-класс унаслеовал от SingleObjectMixin
    # queryset может быть как передан, так и не передан
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
