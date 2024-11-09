# Generated by Django 4.2.1 on 2024-09-19 10:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0006_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ttype',
            field=models.CharField(choices=[('Checkbox', 'Checkbox (использует синтаксис YAML)'), ('Input', 'Input')], default='Input', max_length=255, verbose_name='Тип вопроса'),
        ),
        migrations.AddField(
            model_name='subjtest',
            name='questions_num',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество вопросов'),
        ),
    ]