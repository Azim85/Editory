# Generated by Django 3.2.2 on 2021-07-05 10:59

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('resume', models.FileField(upload_to='resume/')),
                ('is_agree', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(blank=True, upload_to='news/')),
                ('material_name', models.CharField(max_length=100)),
                ('material_name_ru', models.CharField(max_length=100, null=True)),
                ('material_name_en', models.CharField(max_length=100, null=True)),
                ('material_name_uz', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('description_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('others', ckeditor_uploader.fields.RichTextUploadingField()),
                ('others_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('others_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('others_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='TopResearches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='top_researches/')),
                ('title', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('author', models.CharField(max_length=100)),
                ('author_ru', models.CharField(max_length=100, null=True)),
                ('author_en', models.CharField(max_length=100, null=True)),
                ('author_uz', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('description_uz', models.TextField(null=True)),
                ('more', models.TextField()),
                ('more_ru', models.TextField(null=True)),
                ('more_en', models.TextField(null=True)),
                ('more_uz', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
