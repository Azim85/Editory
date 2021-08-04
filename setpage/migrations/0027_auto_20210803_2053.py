# Generated by Django 3.2.2 on 2021-08-03 15:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setpage', '0026_auto_20210803_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencesmodel',
            name='text5',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='conferencesmodel',
            name='text4',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='conferencesmodel',
            name='text4_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='conferencesmodel',
            name='text4_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='conferencesmodel',
            name='text4_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True),
        ),
    ]
