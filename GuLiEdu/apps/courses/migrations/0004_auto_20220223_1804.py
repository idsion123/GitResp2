# Generated by Django 3.1.7 on 2022-02-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20220223_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoinfo',
            name='video',
            field=models.FileField(default='', max_length=200, upload_to='video/', verbose_name='视频链接'),
        ),
    ]
