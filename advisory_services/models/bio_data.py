from django.db import models


class BioData(models.Model):
    name = models.CharField(
        verbose_name='Fullnames',
        max_length=200)
    email = models.EmailField()
    dob = models.DateTimeField(verbose_name='Date of Birth')
    cell = models.CharField(
        verbose_name='Cell number',
        max_length=200)
    education = models.CharField(
        verbose_name='Education',
        max_length=200)
    occupation = models.CharField(
        verbose_name='Occupation',
        max_length=200)