# Generated by Django 3.2.5 on 2022-02-13 06:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date_posted',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
