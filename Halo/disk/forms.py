from django import forms

# Форма регистрации
from .models import DiskUser
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


# Регистрацция
class RegisterUserForm(forms.ModelForm):
    # Полное объявление - обязательно для заполнения:
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                help_text='Введите тот же самый пароль еще раз для проверки')

    # Валидация пароля
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    # Проверка совпадения введеннных паролей
    def clean(self):
        super().clean()
        # cleaned_data = super(RegisterUserForm, self).clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают',
                code='password_mismatch'
            )
            }
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = DiskUser
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name')


class ChangeUserInfoForm(forms.ModelForm):
    # Выполняем полное объявление поля email модели DiskUser
    # Так как оно обязательно
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')
    class Meta:
        model = DiskUser
        fields = ('username', 'email', 'first_name', 'last_name')