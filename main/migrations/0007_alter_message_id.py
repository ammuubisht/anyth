# Generated by Django 3.2.5 on 2022-02-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]