# Generated by Django 2.2 on 2019-10-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0010_auto_20191002_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecthastechnicalsolutions',
            name='tech_sol',
            field=models.ManyToManyField(to='productsapp.TechnicalSolutions'),
        ),
    ]
