# Generated by Django 3.2.2 on 2021-07-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_topic_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='news/'),
        ),
    ]
