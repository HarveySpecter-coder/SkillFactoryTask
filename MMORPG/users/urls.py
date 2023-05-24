from django.urls import path
from .views import login, registration, profile, logout, check_email

app_name = 'users'
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name = 'registration'),
    path('profile/', profile, name = 'profile'),
    path('logout/', logout, name = 'logout'),
    path('registration/check-email/', check_email, name = 'check_email'),
]