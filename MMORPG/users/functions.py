from random import randint
from django.core.mail import EmailMultiAlternatives
from MMORPG.settings import DEFAULT_FROM_EMAIL
from django.template.loader import render_to_string

def send_verify_mail(request) -> int:
    secret_code = randint(1421, 9836)
    user_email = request['email']
    username = request['username']
    context = {'secret_code': secret_code, 'username':username}
    html_content = render_to_string('users/email_for_new_user.html', context)
    msg = EmailMultiAlternatives(
        subject='Вы зарегистрировались на сайте MMORPG',
        body=str(secret_code),
        from_email=DEFAULT_FROM_EMAIL,
        to=(user_email,)
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return secret_code