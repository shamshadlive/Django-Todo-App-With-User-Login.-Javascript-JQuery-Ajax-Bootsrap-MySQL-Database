# Generated by Django 4.1 on 2022-08-31 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='userID',
            field=models.CharField(default='1', max_length=200),
        ),
    ]
