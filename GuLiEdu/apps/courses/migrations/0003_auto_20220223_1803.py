# Generated by Django 3.1.7 on 2022-02-23 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20220222_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoinfo',
            name='url',
        ),
        migrations.AddField(
            model_name='videoinfo',
            name='video',
            field=models.FileField(default='wwww.baidu.com', max_length=200, upload_to='video/', verbose_name='视频链接'),
        ),
    ]
