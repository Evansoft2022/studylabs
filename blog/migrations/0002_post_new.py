# Generated by Django 3.2.8 on 2022-03-15 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='new',
            field=models.BooleanField(default=True),
        ),
    ]
