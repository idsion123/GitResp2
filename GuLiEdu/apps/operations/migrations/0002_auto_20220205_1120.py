# Generated by Django 3.1.7 on 2022-02-05 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operations', '0001_initial'),
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userlove',
            name='love_man',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='收藏人'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='study_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courseinfo', verbose_name='学习课程'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='study_man',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学习人'),
        ),
        migrations.AddField(
            model_name='usercomment',
            name='comment_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courseinfo', verbose_name='评论课程'),
        ),
        migrations.AddField(
            model_name='usercomment',
            name='comment_man',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论人'),
        ),
        migrations.AlterUniqueTogether(
            name='usercourse',
            unique_together={('study_man', 'study_course')},
        ),
    ]
