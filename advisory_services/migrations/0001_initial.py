# Generated by Django 4.1.2 on 2022-10-09 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BioData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Fullnames")),
                ("email", models.EmailField(max_length=254)),
                ("dob", models.DateTimeField(verbose_name="Date of Birth")),
                ("cell", models.CharField(max_length=200, verbose_name="Cell number")),
                (
                    "education",
                    models.CharField(max_length=200, verbose_name="Education"),
                ),
                (
                    "occupation",
                    models.CharField(max_length=200, verbose_name="Occupation"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=200, verbose_name="Fullnames")),
                (
                    "message_body",
                    models.CharField(max_length=300, verbose_name="Message Body"),
                ),
                (
                    "recipient",
                    models.CharField(max_length=200, verbose_name="Recipient"),
                ),
                (
                    "message_platform",
                    models.CharField(max_length=200, verbose_name="Message Platform"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ServicePrograme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField(verbose_name="Start date")),
                ("start_end", models.DateField(verbose_name="End date")),
                (
                    "age_group",
                    models.CharField(max_length=100, verbose_name="Age group"),
                ),
                ("gender", models.CharField(max_length=50, verbose_name="Gender")),
                (
                    "education",
                    models.CharField(max_length=200, verbose_name="Education"),
                ),
                (
                    "program_description",
                    models.CharField(
                        max_length=200, verbose_name="Program Description"
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="advisory_services.message",
                    ),
                ),
            ],
        ),
    ]