# Generated by Django 2.2 on 2019-10-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0004_auto_20191030_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, verbose_name='слаг'),
        ),
    ]
