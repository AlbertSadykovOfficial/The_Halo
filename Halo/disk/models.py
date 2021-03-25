from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class DiskUser(AbstractUser):
    # Явное удлаение объявлений при удалении пользователя
    # Может не будет работать
    """def delete(self, *args, **kwargs):
        for poster in self.poster_set.all():
            poster.delete()
        super().delete(*args, **kwargs)
    """

    class Meta(AbstractUser.Meta):
        pass