# Generated by Django 3.2.5 on 2022-02-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_message_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='uid',
            field=models.CharField(max_length=20),
        ),
    ]