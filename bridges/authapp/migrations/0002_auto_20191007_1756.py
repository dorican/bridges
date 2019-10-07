# Generated by Django 2.2 on 2019-10-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='address',
            field=models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='form_company',
            field=models.CharField(blank=True, choices=[(None, 'не указано'), ('IP', 'ИП'), ('OOO', 'ООО'), ('OAO', 'ОАО'), ('ZAO', 'ЗАО'), ('PAO', 'ПАО'), ('AO', 'АО'), ('NAO', 'НАО'), ('NKO', 'НКО'), ('ANO', 'АНО'), ('GBU', 'ГБУ')], max_length=3, null=True, verbose_name='Форма'),
        ),
    ]
