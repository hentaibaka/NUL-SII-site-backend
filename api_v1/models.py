from django.db import models
from .utils import handle_project_photo, handle_employee_photo


class Publication(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False, verbose_name='Название')
    authors = models.CharField(max_length=256, blank=False, null=False, verbose_name='Авторы')
    journal = models.CharField(max_length=256, blank=False, null=False, verbose_name='Журнал')
    link = models.URLField(max_length=256, blank=True, null=True, verbose_name='Ссылка')

    class Meta():
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'

    def __str__(self) -> str:
        return self.title

class Employee(models.Model):
    photo = models.ImageField(upload_to=handle_employee_photo, verbose_name='Фото')
    post = models.CharField(max_length=64, blank=False, null=False, verbose_name='Должность')
    last_name = models.CharField(max_length=32, blank=False, null=False, verbose_name='Фамилия')
    first_name = models.CharField(max_length=32, blank=False, null=False, verbose_name='Имя')
    patronymic = models.CharField(max_length=32, blank=True, null=True, verbose_name='Отчество')
    link = models.URLField(max_length=256, blank=True, null=True, verbose_name='Ссылка')

    class Meta():
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} {self.patronymic}'
    
class Contact(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    question = models.TextField(verbose_name='Вопрос')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Время обращения')

    class Meta():
        verbose_name_plural = 'Обращения'
        verbose_name = 'Обращение'

    def __str__(self) -> str:
        return self.email

class Project(models.Model):
    class StatusChoices(models.IntegerChoices):
        REALIZED = (0, 'Реализовано')
        IN_PROGRESS = (1, 'разрабатывается')
    
    class TypeChoices(models.IntegerChoices):
        PHOTO = (0, 'Фото')
        VIDEO = (1, 'Видео')

    photo = models.ImageField(upload_to=handle_project_photo, verbose_name='Фото')
    title = models.CharField(max_length=256, blank=False, null=False, verbose_name='Название')
    authors = models.ManyToManyField(Employee, blank=True, verbose_name='Авторы')
    instruction = models.TextField(verbose_name='Инструкция')
    description = models.TextField(verbose_name='Описание')
    is_realized = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), StatusChoices.choices)), 
                                 default=StatusChoices.REALIZED, verbose_name='Статус')
    type = models.IntegerField(choices=TypeChoices.choices, blank=False, null=False, verbose_name='Тип')
    slug = models.SlugField(unique=True, max_length=256, blank=True, null=True, verbose_name='Slug')
    
    class Meta():
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'

    def __str__(self) -> str:
        return self.title
