from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CategoryCompany(models.Model):
    """ модель содержит информацию о категории компании,
    например: проектный институт, подрядная организация, заказчик и др. """
    name = models.CharField(verbose_name='Категория компании*', max_length=50, unique=True)
    description = models.CharField(verbose_name='Описание категории', max_length=300, default='', null=True, blank=True)

    class Meta:
        verbose_name = "Категорию компании"
        verbose_name_plural = "Категории компаний"
        ordering = ["name"]

    def __str__(self):
        return self.name.title()


class FormCompany(models.Model):
    """ модель содержит организационно-правовые формы предприятия,
    например, ООО, ИП, ОАО, ЗАО и др. """
    name = models.CharField(verbose_name='Форма компании*', max_length=30, unique=True)
    description = models.CharField(verbose_name='Описание формы', max_length=300, default='', null=True, blank=True)

    class Meta:
        verbose_name = "Форму компании"
        verbose_name_plural = "Формы компаний"
        ordering = ["name"]

    def __str__(self):
        return self.name.upper()


class Company(models.Model):
    """модель содержит подробную информацию о компании"""

    name = models.CharField(verbose_name='Полное название*', max_length=70)
    short = models.CharField(verbose_name='Короткое название', max_length=30, blank=True, null=True)
    form = models.ForeignKey(FormCompany, on_delete=models.PROTECT, verbose_name='Форма', blank=True, null=True)
    category = models.ForeignKey(CategoryCompany, on_delete=models.PROTECT, verbose_name='Категория компании*')
    logo = models.ImageField(verbose_name='логотип', upload_to='logo_company', blank=True, null=True)
    inn = models.BigIntegerField(verbose_name='ИНН*', unique=True)
    city = models.CharField(verbose_name='Город', max_length=30, default='', null=True, blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=300, default='', null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=30, default='', null=True, blank=True)
    email = models.CharField(verbose_name='Эл. почта', max_length=30, default='', null=True, blank=True)

    class Meta:
        verbose_name = "Новую компанию"
        verbose_name_plural = "Компании"
        ordering = ["name"]

    def __str__(self):
        return self.name.title()


class Users(AbstractUser):
    """ модель содержит информацию о всех пользователях, включая superuser, сотрудников компании
    и простых пользователей.
    У AbstractUser есть поля: password, last_login, first_name, last_name, email, is_superuser, is_staff,
    # is_active и date_joined.
    Создадим дополнительные поля. """
    GENDER_CHOICES = (
        (None, 'не указан'),
        ('male', 'мужчина'),
        ('female', 'женщина'),
    )
    username = models.CharField(verbose_name='Логин*', max_length=50, unique=True)  # переопределили из-за verbose_name
    patronymic = models.CharField(verbose_name='Отчество', max_length=50, default='', null=True, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    birthday = models.DateField(verbose_name='День рождения', blank=True, null=True)
    phone = models.CharField(verbose_name='Телефон*', max_length=50, default='не указан')
    city = models.CharField(verbose_name='Город', max_length=50, default='', null=True, blank=True)
    company = models.ManyToManyField(Company, verbose_name='Компания')
    position = models.CharField(verbose_name='Должность', max_length=50, default='', null=True, blank=True)
    project = models.CharField(verbose_name='Проект', max_length=50, default='', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        verbose_name = "Пользователя"
        ordering = ['-date_joined']
