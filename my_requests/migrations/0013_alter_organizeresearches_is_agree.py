# Generated by Django 3.2.2 on 2021-05-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0012_alter_organizeresearches_is_agree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizeresearches',
            name='is_agree',
            field=models.BooleanField(error_messages={'required': 'You must accept the terms and conditions'}),
        ),
    ]
