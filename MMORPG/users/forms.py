from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms
from django.core.exceptions import ValidationError

class UserLoginForm(AuthenticationForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4', 'placeholder':'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control py-4', 'placeholder':'Введите пароль'}))
    class Meta:
        model = User
        field = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4', 'placeholder':'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4', 'readonly':True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')

class SecretCodeForm(forms.Form):
    code = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'secret_code_input',
        'type':'number',
        'id':'secret_code_input',
        'autofocus':'True',
        'inputmode':'numeric',
        'placeholder':'----'}),
        error_messages={'invalid':'Вы ввели неверный код'})

    def clean_code(self):
        user_entered_code = self.cleaned_data['code']
        if user_entered_code != self.initial['secret_code']:
            raise ValidationError('Вы ввели неверный код')
        return

