# Generated by Django 3.1.7 on 2022-02-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220206_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_start',
            field=models.BooleanField(default=False, verbose_name='是否激活'),
        ),
    ]
