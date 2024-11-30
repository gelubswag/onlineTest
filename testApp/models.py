from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from datetime import datetime
import random


class Subject(models.Model):
    name = models.CharField(verbose_name="Дисциплина", max_length=250, unique=True)

    def __str__(self) -> str:
        return self.name


class SubjTest(models.Model):
    name = models.CharField(verbose_name="Название теста", max_length=250)
    subj = models.ForeignKey(
        Subject, verbose_name="Дисциплина", on_delete=models.CASCADE
    )
    questions_num = models.IntegerField(
        verbose_name="Максимальное количество вопросов",
        validators=[MinValueValidator(1)],
        default=1,
    )

    test_questions_num = models.IntegerField(
        verbose_name="Вопросов в тесте", validators=[MinValueValidator(1)], default=1
    )

    def __str__(self) -> str:
        return self.subj.name + "> " + self.name


# Create your models here.


class Question(models.Model):
    test = models.ForeignKey(SubjTest, verbose_name="Тест", on_delete=models.CASCADE)
    image = models.ImageField(
        verbose_name="Изображение", blank=True, null=True, upload_to="media/"
    )
    imageURL = models.URLField(
        verbose_name="Ссылка на изображение", blank=True, null=True, default=""
    )
    text = models.TextField(verbose_name="Вопрос", max_length=5048, default="")
    weight = models.IntegerField(
        verbose_name="Вес вопроса", validators=[MinValueValidator(1)], default=1
    )
    optionsNum = models.IntegerField(
        verbose_name="Количество вариантов ответа",
        validators=[MinValueValidator(1)],
        default=1,
    )

    def __str__(self):
        return self.test.subj.name + "> " + self.test.name + "> " + self.text[:5]


class Option(models.Model):
    quest = models.ForeignKey(
        Question, verbose_name="Вопрос", on_delete=models.CASCADE, null=True, blank=True
    )
    text = models.TextField(verbose_name="Текст", max_length=5048, default="")
    image = models.ImageField(
        verbose_name="Изображение", blank=True, upload_to="media/", null=True
    )
    imageURL = models.URLField(
        verbose_name="Ссылка на изображение", blank=True, null=True, default=""
    )
    isRight = models.BooleanField(
        verbose_name="Верный ответ?", default=False, blank=True
    )

    def __str__(self):
        return (
            str(self.quest)
            + "> "
            + self.text
            + ["| Без иозображения", "| С изображениеи"][
                bool(bool(self.image) + bool(self.imageURL))
            ]
            + "> "
            + ["Wrong", "Right"][self.isRight]
        )


class UserTest(models.Model):
    test = models.ForeignKey(SubjTest, verbose_name="Тест", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    time_start = models.DateTimeField(verbose_name="Начало", default=datetime.now())
    time_end = models.DateTimeField(verbose_name="Конец", default=datetime.now())
    points = models.IntegerField(verbose_name="Баллы", default=0)
    isFinished = models.BooleanField(default=False)
    question_pool = models.JSONField(verbose_name="Пул вопросов", default=list)

    def __str__(self):
        return (
            ["Not Finished ", "Finished "][self.isFinished]
            + self.user.username
            + "> "
            + self.test.subj.name
            + "> "
            + self.test.name
        )

    def make_question_pool(self):
        self.question_pool = [i.id for i in Question.objects.filter(test=self.test)]
        random.shuffle(self.question_pool)
        self.question_pool = self.question_pool[0 : self.test.test_questions_num]
        self.save()
        return self.question_pool


class UserAnswer(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    test = models.ForeignKey(UserTest, verbose_name="Тест", on_delete=models.CASCADE)
    quest = models.ForeignKey(
        Question, verbose_name="Вопрос", on_delete=models.CASCADE, null=True, blank=True
    )
    opt = models.ForeignKey(
        Option,
        verbose_name="Вариант ответа",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    answer = models.BooleanField(default=False)

    def __str__(self):
        return self.test.user.username + "> " + str(self.opt)
