from django.db import models

class Subject(models.Model):
    name = models.CharField(verbose_name="Дисциплина", max_length=250, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
class SubjTest(models.Model):
    name = models.CharField(verbose_name="Название теста", max_length=250)
    subj = models.ForeignKey( Subject,verbose_name="Дисциплина",on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.subj.name + "> " + self.name
# Create your models here.

class Question:
    test = models.ForeignKey(SubjTest, verbose_name="Тест", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Вопрос", max_length=500)
    right = models.TextField(verbose_name="Правильный ответ", max_length=500)