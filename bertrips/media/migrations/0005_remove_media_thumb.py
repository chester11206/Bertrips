# Generated by Django 2.0.6 on 2018-07-03 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_auto_20180703_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='thumb',
        ),
    ]
