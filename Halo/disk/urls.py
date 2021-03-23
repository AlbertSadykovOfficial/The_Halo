from django.urls import path, re_path

from .views import index
from .views import other_page
from .views import upload_file

from .views import RegisterUserView, RegisterDoneView
from .views import DiskLoginView, DiskLogoutView
from .views import DeleteUserView

# Добавляем пространство имен
# Это поможет при рендеринге, можно указывать
# <namespace>:<app_name> <=> disk:upload
app_name = 'disk'

urlpatterns = [
    #    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),

    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),

    # Путь к странцие входа
    path('accounts/login/', DiskLoginView.as_view(), name='login'),
    # Или: path('accounts/login/', LoginView.as_view(template_name='disk/login.html'), name='login')
    # Имя шаблона выаодимой страницы передается через page
    path('accounts/logout/', DiskLogoutView.as_view(), name='logout'),

    path('upload/', upload_file, name='upload'),
    #<str:folder>/ \D+.*
    re_path(r'^(?P<folder>\D+/)', other_page, name='other'),
    path('', index, name='index'),
]
