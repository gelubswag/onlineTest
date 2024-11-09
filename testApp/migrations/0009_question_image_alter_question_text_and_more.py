# Generated by Django 4.2.1 on 2024-09-20 09:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0008_alter_subjtest_questions_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(default='', max_length=5048, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='subjtest',
            name='questions_num',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество вопросов'),
        ),
    ]