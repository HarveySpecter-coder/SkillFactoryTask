from .functions import send_verify_mail
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, SecretCodeForm
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('board:index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            secret_code = send_verify_mail(request.POST)
            request.session['secret_code'] = secret_code
            return HttpResponseRedirect(reverse('users:check_email'))
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title':'Ваш профиль', 'form':form}
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('board:index'))

def check_email(request):
    secret_code = request.session.get('secret_code')
    initial_data = {'secret_code': secret_code}
    if request.method == 'POST':
        form = SecretCodeForm(initial=initial_data, data=request.POST)
        if form.is_valid():
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = SecretCodeForm(initial=initial_data)
    context = {'form':form}
    return render(request, 'users/email_verification.html', context)