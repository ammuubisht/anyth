# Generated by Django 3.2.5 on 2022-02-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20220211_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]