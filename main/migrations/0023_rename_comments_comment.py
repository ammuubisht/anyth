# Generated by Django 3.2.5 on 2022-02-15 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
