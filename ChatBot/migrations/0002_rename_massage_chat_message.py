# Generated by Django 4.0.6 on 2022-07-09 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChatBot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='massage',
            new_name='message',
        ),
    ]
