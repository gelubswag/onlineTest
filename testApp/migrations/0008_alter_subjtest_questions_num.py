# Generated by Django 4.2.1 on 2024-09-19 11:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0007_question_ttype_subjtest_questions_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjtest',
            name='questions_num',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество вопросов'),
        ),
    ]