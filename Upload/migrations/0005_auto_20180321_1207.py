# Generated by Django 2.0.3 on 2018-03-21 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0004_auto_20180321_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
