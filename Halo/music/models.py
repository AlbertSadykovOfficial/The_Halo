from django.db import models
from django.forms.models import modelform_factory


class MediaModel(models.Model):
    media_file = models.FileField(upload_to='songs/')


MediaForm = modelform_factory(MediaModel, fields={'media_file'})
