# Generated by Django 2.0.3 on 2018-03-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0002_image_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='cordinates',
            field=models.CharField(default='0 0', max_length=256),
        ),
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateField(),
        ),
    ]
