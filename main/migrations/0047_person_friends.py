# Generated by Django 3.2.5 on 2022-02-26 06:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0046_person_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(default=None, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
