from django.db import models
from django.utils import timezone



# Модель Детский Кружок
class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    teacher_name = models.CharField(max_length=100, verbose_name='ФИО руководителя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Уроки'
        verbose_name = 'Урок'
        ordering = ['name']

# Модель Расписание Занятий Кружка
class Schedule(models.Model):
    kids_circle = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='schedules', verbose_name='Детский Кружок')
    date = models.DateField(verbose_name='Дата занятия')
    time = models.TimeField(verbose_name='Время занятия')

    def __str__(self):
        return f"{self.kids_circle.name} - {self.date} {self.time}"

    class Meta:
        verbose_name_plural = 'Расписания занятий кружков'
        verbose_name = 'Расписание занятия кружка'
        ordering = ['date', 'time']

# Модель Дети
class Child(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic} {self.birth_date}"

    class Meta:
        verbose_name_plural = 'Дети'
        verbose_name = 'Ребенок'
        ordering = ['-last_name', '-first_name']

# Модель Запись
class Record(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='records', verbose_name='Расписание')
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='records', verbose_name='Ребенок')

    def __str__(self):
        return f"{self.child.last_name}{self.child.last_name} - {self.date} {self.time}"

    class Meta:
        verbose_name_plural = 'Информация о записи в каждый кружок'
        verbose_name = 'Информация о записи в отдельный кружок'
        ordering = ['schedule__date', 'schedule__time']




