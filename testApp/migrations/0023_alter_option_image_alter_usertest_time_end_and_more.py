# Generated by Django 4.2.1 on 2024-10-25 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0022_useranswer_user_alter_usertest_isfinished_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='image',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_end',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 25, 20, 3, 0, 602351), verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 25, 20, 3, 0, 602351), verbose_name='Начало'),
        ),
    ]