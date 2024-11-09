# Generated by Django 4.2.1 on 2024-10-24 16:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testApp', '0021_alter_usertest_isfinished_alter_usertest_time_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='isFinished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_end',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 19, 12, 35, 535044), verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 19, 12, 35, 535044), verbose_name='Начало'),
        ),
    ]
