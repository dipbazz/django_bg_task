from django.conf import settings
from django.core.mail import send_mail

from django_bg_task import celery_app


@celery_app.task()
def send_mail_task(subject, message, recipient_list, from_email=settings.EMAIL_HOST_USER,
              fail_silently=False, auth_user=None, auth_password=None,
              connection=None, html_message=None):
    send_mail(subject, message, from_email, recipient_list,
              fail_silently=fail_silently, auth_user=auth_user, auth_password=auth_password,
              connection=connection, html_message=html_message)

