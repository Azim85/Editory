# Generated by Django 3.2.2 on 2021-08-05 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0017_alter_translation_word_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translation',
            name='word_amount',
        ),
    ]
