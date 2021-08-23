# Generated by Django 3.2.2 on 2021-08-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffs',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='text_uz',
            field=models.TextField(null=True),
        ),
    ]