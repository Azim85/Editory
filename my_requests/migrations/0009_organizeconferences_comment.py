# Generated by Django 3.2.2 on 2021-07-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0008_scopus'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizeconferences',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
