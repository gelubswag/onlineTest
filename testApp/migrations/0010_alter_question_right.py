# Generated by Django 4.2.1 on 2024-09-20 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0009_question_image_alter_question_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='right',
            field=models.TextField(default='', max_length=500, verbose_name='Правильный ответ'),
        ),
    ]
