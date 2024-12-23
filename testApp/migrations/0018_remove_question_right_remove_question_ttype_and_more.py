# Generated by Django 4.2.1 on 2024-09-29 08:20

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0017_alter_usertest_time_end_alter_usertest_time_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='right',
        ),
        migrations.RemoveField(
            model_name='question',
            name='ttype',
        ),
        migrations.AddField(
            model_name='question',
            name='optionsNum',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество вариантов ответа'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_end',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 29, 11, 20, 22, 448324), verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 29, 11, 20, 22, 448324), verbose_name='Начало'),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=5048, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, upload_to='media/options', verbose_name='Изображение')),
                ('isRight', models.BooleanField(default=False, verbose_name='Верный ответ?')),
                ('quest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testApp.question', verbose_name='Вопрос')),
            ],
        ),
        migrations.AddField(
            model_name='useranswer',
            name='opt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testApp.option', verbose_name='Вариант ответа'),
        ),
    ]
