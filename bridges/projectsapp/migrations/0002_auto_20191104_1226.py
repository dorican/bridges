# Generated by Django 2.2 on 2019-11-04 09:26

from django.db import migrations
import imagekit.models.fields
import projectsapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='users/avatar/no_avatar.png', upload_to='projects_images/avatars', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=projectsapp.models.image_upload_to, verbose_name='фотографии проекта'),
        ),
    ]
