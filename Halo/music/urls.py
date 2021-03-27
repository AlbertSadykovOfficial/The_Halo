from django.urls import path

from .views import index, media_create
app_name = 'music'

urlpatterns = [
    path('add/', media_create, name='media_create'),
    path('', index, name='index'),
]
