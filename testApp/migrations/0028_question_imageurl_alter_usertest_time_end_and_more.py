# Generated by Django 5.1 on 2024-11-12 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0027_alter_option_image_alter_usertest_time_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='imageURL',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_end',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 12, 17, 54, 26, 327588), verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 12, 17, 54, 26, 327588), verbose_name='Начало'),
        ),
    ]
