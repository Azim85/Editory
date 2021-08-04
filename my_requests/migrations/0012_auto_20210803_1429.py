# Generated by Django 3.2.2 on 2021-08-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0011_merge_0007_language_file_0010_getgrant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translation',
            name='extra',
        ),
        migrations.AlterField(
            model_name='translation',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Russian', 'Russian'), ('Uzbek', 'Uzbek')], max_length=100),
        ),
    ]
