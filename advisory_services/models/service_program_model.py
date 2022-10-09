from django.db import models

from .message import Message


class ServicePrograme(models.Model):

    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    start_date = models.DateField(
        verbose_name='Start date')
    
    start_end = models.DateField(
        verbose_name='End date')

    age_group = models.CharField(
        verbose_name='Age group',
        max_length=100)

    gender = models.CharField(
        verbose_name='Gender',
        max_length=50)

    education = models.CharField(
        verbose_name='Education',
        max_length=200)
    
    program_description = models.CharField(
        verbose_name='Program Description',
        max_length=200)
