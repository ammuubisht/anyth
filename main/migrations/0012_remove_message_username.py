# Generated by Django 3.2.5 on 2022-02-11 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20220211_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='username',
        ),
    ]
