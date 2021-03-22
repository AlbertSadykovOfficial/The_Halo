from django.urls import path
from .views import index
from .views import upload_file

urlpatterns = [
    path('upload/', upload_file),
    path('', index),
]