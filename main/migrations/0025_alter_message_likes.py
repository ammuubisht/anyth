# Generated by Django 3.2.5 on 2022-02-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_message_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
