# Generated by Django 4.2.1 on 2023-05-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("sname", models.CharField(max_length=100)),
                ("sid", models.IntegerField(primary_key=True, serialize=False)),
                ("tname", models.CharField(max_length=100)),
            ],
        ),
    ]
