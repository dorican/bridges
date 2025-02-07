# Generated by Django 2.2 on 2019-11-14 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20191107_1404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'default_permissions': ('add', 'change', 'delete'), 'ordering': ['-date_joined'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='companyusers',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='authapp.Company', verbose_name='Компания'),
        ),
    ]
