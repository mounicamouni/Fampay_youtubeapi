# Generated by Django 3.2 on 2021-04-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fampayapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='channel_title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='videos',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='videos',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
