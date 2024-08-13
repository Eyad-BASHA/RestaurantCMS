"""Send email to user for activation his account"""

from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator


def send_activation_email(user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    activation_link = reverse("activate", kwargs={"uidb64": uid, "token": token})
    activation_url = f"{settings.FRONTEND_URL}{activation_link}"

    subject = "Activate your account"
    message = render_to_string(
        "account_activation_email.html",
        {
            "user": user,
            "activation_url": activation_url,
        },
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
