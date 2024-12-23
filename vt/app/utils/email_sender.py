# utils/email_sender.py
from django.core.mail import send_mail

def send_report(email, subject, message, attachment_path):
    send_mail(
        subject,
        message,
        'sarahmokrani96@gmail.com',
        [email],
        fail_silently=False,
    )
