# Generated by Django 3.2.5 on 2022-02-16 10:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0030_alter_message_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='likes',
            field=models.ManyToManyField(default=None, null=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
