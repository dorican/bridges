# Generated by Django 2.2 on 2019-11-04 09:04

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='users/avatar/no_avatar.png', upload_to='users/avatar', verbose_name='Аватар'),
        ),
    ]
