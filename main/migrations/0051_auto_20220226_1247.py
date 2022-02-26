# Generated by Django 3.2.5 on 2022-02-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_auto_20220226_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={},
        ),
        migrations.AlterModelManagers(
            name='person',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='password',
        ),
        migrations.RemoveField(
            model_name='person',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='person',
            name='username',
        ),
        migrations.AlterField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(blank=True, default=None, related_name='_main_person_friends_+', to='main.Person'),
        ),
    ]