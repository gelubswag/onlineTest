# Generated by Django 4.2.1 on 2024-09-26 10:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testApp', '0011_alter_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='weight',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Вес вопроса'),
        ),
        migrations.CreateModel(
            name='UserTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(verbose_name='Начало')),
                ('time_end', models.DateTimeField(verbose_name='Конец')),
                ('points', models.IntegerField(verbose_name='Баллы')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.subjtest', verbose_name='Тест')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(default='', max_length=500, verbose_name='Ответ')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.usertest', verbose_name='Тест')),
            ],
        ),
    ]
