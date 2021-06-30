# Generated by Django 3.2.2 on 2021-05-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0016_proofreading_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='proofreading',
            name='is_agree',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='proofreading',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
