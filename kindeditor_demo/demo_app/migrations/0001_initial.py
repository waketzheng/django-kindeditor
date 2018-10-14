# Generated by Django 2.0.3 on 2018-03-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExampleModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(verbose_name="content")),
                (
                    "title",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
            options={"abstract": False},
        )
    ]
