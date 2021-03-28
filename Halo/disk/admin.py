from django.contrib import admin
from .models import DiskUser


# Register your models here.
class DiskUserAdmin(admin.ModelAdmin):
    # Вы одим строковое предствалени записи (имя пользователя как в AbstractUser)
    list_display = ('__str__', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('is_staff', 'is_superuser'),
              'groups', 'user_permissions',
              ('last_login', 'date_joined')
              )
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(DiskUser, DiskUserAdmin)
