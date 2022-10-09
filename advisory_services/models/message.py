from django.db import models


class Message(models.Model):
    subject = models.CharField(
        verbose_name='Fullnames',
        max_length=200)

    message_body = models.CharField(
        verbose_name='Message Body',
        max_length=300)

    recipient = models.CharField(
        verbose_name='Recipient',
        max_length=200)

    message_platform = models.CharField(
        verbose_name='Message Platform',
        max_length=200)
