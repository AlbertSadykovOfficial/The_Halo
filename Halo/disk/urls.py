from django.urls import path, re_path

from .views import index
from .views import about
from .views import other_page
from .views import change_name, \
                   upload_files, \
                   create_file,\
                   delete_file,\
                   delete_folder,\
                   create_folder,\
                   download_file, \
                   download_folder

from .views import RegisterUserView, RegisterDoneView
from .views import DiskLoginView, DiskLogoutView
from .views import DeleteUserView
from .views import DiskPasswordChangeView
from .views import ChangeUserInfoView

# Добавляем пространство имен
# Это поможет при рендеринге, можно указывать
# <namespace>:<app_name> <=> disk:upload
app_name = 'disk'

urlpatterns = [
    #    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),

    path('accounts/password/change/', DiskPasswordChangeView.as_view(), name='password_change'),

    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),

    # Путь к странцие входа
    path('accounts/login/', DiskLoginView.as_view(), name='login'),
    path('accounts/logout/', DiskLogoutView.as_view(), name='logout'),

    # sha_256(function_name) -> token
    re_path(r'^63b8d67eb1ca393b5e69b31a5d126d553a3fb94afd7a60c90049e66c66c6b891/(?P<path>.*)', change_name, name='change_name'),
    re_path(r'^463d52e2aaa10e704eb0b24dea0eea8e9b86e38d52c28993eeebcf6ec01ec347/(?P<path>.*)', create_file, name='create_file'),
    re_path(r'^87b5c6b2b1e3e19601b421b8b81e199e4d27876d045610b5dcf078017caee694/(?P<path>.*)', delete_file, name='delete_file'),
    re_path(r'^5b53fba3b9601c8aa7ff13ce2d164f427a54f49b8873fa382e310f2162e0db08/(?P<path>.*)', create_folder, name='create_folder'),
    re_path(r'^e2a7114fca4f6f72dbfedc267c06cd4ff38644dbf11bae90efdf4d19c7ee7474/(?P<path>.*)', delete_folder, name='delete_folder'),
    re_path(r'^a3b2ceb1f2d110bf6c5f9f261a6f448a5be06e2e1a515e3e65bf7943300f89a3/(?P<path>.*)', upload_files, name='upload_files'),

    re_path(r'^download_folder/(?P<path>.*)', download_folder, name='download_folder'),
    re_path(r'^download_file/(?P<path>.*)', download_file, name='download_file'),
    path('about/', about, name='about'),
    re_path(r'^(?P<folder>.*)', other_page, name='other'),
    path('', index, name='index'),
]
