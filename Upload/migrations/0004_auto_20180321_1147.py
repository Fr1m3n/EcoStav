# Generated by Django 2.0.3 on 2018-03-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0003_auto_20180319_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='cordinates',
        ),
        migrations.AddField(
            model_name='image',
            name='coordinates',
            field=models.CharField(default='', max_length=256),
        ),
    ]
