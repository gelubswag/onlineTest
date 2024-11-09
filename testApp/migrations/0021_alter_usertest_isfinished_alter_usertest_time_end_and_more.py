# Generated by Django 4.2.1 on 2024-10-24 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0020_alter_option_isright_alter_usertest_time_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertest',
            name='isFinished',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_end',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 18, 51, 20, 257103), verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 24, 18, 51, 20, 257103), verbose_name='Начало'),
        ),
    ]