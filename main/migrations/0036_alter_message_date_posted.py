# Generated by Django 3.2.5 on 2022-02-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_message_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
