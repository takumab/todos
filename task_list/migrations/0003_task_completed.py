# Generated by Django 2.0.3 on 2018-04-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0002_auto_20180402_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
