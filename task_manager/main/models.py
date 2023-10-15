from django.db import models

"""
Класс Task создан для описания записи/задачи/заметки, 
где title - заголовок, который специально ограничен 50 символами, а task - текст заметки.

Класс Meta используется для изменения отображения задач в админке в единичном и множественном числе.
"""


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
