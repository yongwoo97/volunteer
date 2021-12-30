from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def sending_email(message_data, who):
    mail_title = '이메일 인증을 완료해주세요'
    email = EmailMessage(mail_title, message_data, to=[who])
    email.send()
    print('hello')
    return

