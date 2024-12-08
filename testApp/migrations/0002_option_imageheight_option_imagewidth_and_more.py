# Generated by Django 5.1.1 on 2024-12-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='imageHeight',
            field=models.PositiveBigIntegerField(default=200, verbose_name='Высота изображения в пикселях'),
        ),
        migrations.AddField(
            model_name='option',
            name='imageWidth',
            field=models.PositiveBigIntegerField(default=200, verbose_name='Ширина изображения в пикселях'),
        ),
        migrations.AddField(
            model_name='question',
            name='imageHeight',
            field=models.PositiveBigIntegerField(default=200, verbose_name='Высота изображения в пикселях'),
        ),
        migrations.AddField(
            model_name='question',
            name='imageWidth',
            field=models.PositiveBigIntegerField(default=200, verbose_name='Высота изображения в пикселях'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_end',
            field=models.DateTimeField(verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_start',
            field=models.DateTimeField(verbose_name='Начало'),
        ),
    ]
