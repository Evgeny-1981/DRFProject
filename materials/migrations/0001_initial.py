# Generated by Django 5.0.7 on 2024-07-22 03:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='наименование курса')),
                ('slug', models.CharField(max_length=120, unique=True, verbose_name='имя слаг')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание курса')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/course_image/', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'db_table': 'course',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='наименование урока')),
                ('slug', models.CharField(max_length=120, unique=True, verbose_name='имя слаг')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание урока')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/lesson_image/', verbose_name='изображение')),
                ('link_video', models.FileField(blank=True, null=True, upload_to='media/lesson_video', verbose_name='видео')),
                ('name_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='урок', to='materials.course', verbose_name='название курса')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'db_table': 'lesson',
                'ordering': ('name',),
            },
        ),
    ]
