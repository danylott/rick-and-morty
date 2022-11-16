# Generated by Django 4.1.3 on 2022-11-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Character",
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
                ("api_id", models.IntegerField(unique=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Alive", "Alive"),
                            ("Dead", "Dead"),
                            ("unknown", "Unknown"),
                        ],
                        max_length=50,
                    ),
                ),
                ("species", models.CharField(max_length=255)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Female", "Female"),
                            ("Male", "Male"),
                            ("Genderless", "Genderless"),
                            ("unknown", "Unknown"),
                        ],
                        max_length=50,
                    ),
                ),
                ("image", models.URLField(max_length=255, unique=True)),
            ],
        ),
    ]