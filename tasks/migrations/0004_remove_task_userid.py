# Generated by Django 4.1 on 2022-08-31 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='userID',
        ),
    ]
