# Generated by Django 3.1.7 on 2022-02-05 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号码')),
                ('course', models.CharField(max_length=20, verbose_name='课程')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '咨询信息',
                'verbose_name_plural': '咨询信息',
            },
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=300, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户评论课程信息',
                'verbose_name_plural': '用户评论课程信息',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户学习课程信息',
                'verbose_name_plural': '用户学习课程信息',
            },
        ),
        migrations.CreateModel(
            name='UserLove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('love_id', models.IntegerField(verbose_name='收藏id')),
                ('love_type', models.IntegerField(choices=[(1, 'org'), (2, 'course'), (3, 'teacher')], verbose_name='收藏类别')),
                ('love_status', models.BooleanField(default=False, verbose_name='收藏状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '收藏信息',
                'verbose_name_plural': '收藏信息',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_man', models.IntegerField(default=0, verbose_name='消息用户')),
                ('message_content', models.CharField(max_length=200, verbose_name='消息内容')),
                ('message_status', models.BooleanField(default=False, verbose_name='消息状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户消息信息',
                'verbose_name_plural': '用户消息信息',
            },
        ),
    ]
