# Generated by Django 2.2 on 2019-10-31 05:51

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='название')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='слаг')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='news_avatars')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='обновлен')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='NewsHasTechnicalSolutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='название конструкции или участка')),
                ('value', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Объем работ')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='newsapp.News', verbose_name='Новость')),
                ('techsol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='productsapp.TechnicalSolutions', verbose_name='Техническое решение')),
            ],
            options={
                'verbose_name': 'Тех решение проекта',
                'verbose_name_plural': 'Тех решения проекта',
            },
        ),
    ]
