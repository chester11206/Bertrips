# Generated by Django 2.0.6 on 2018-07-06 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20180703_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='upload'),
        ),
    ]
