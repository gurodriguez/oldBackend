from django.core.mail import send_mail
from smtplib import SMTPException
from django.conf import settings
from django.template import Context
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_product_notification(product, subject):
    """ Send email when there is a product's change"""
    try:
        html_message = render_to_string('product_notifications.html', {
                                        'subject': subject, 'product': product})
        plain_message = strip_tags(html_message)
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            settings.SYSADMIN,
            html_message=html_message
        )
    except SMTPException as e:
       print('There was an error sending an email.' + e)
    except:
       print("Mail Sending Failed!")
