# Generated by Django 3.2.2 on 2021-08-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0008_researchplatformscontext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proofreading',
            name='choose',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='proofreading',
            name='language_editing',
            field=models.CharField(choices=[('English', 'English'), ('Русский', 'Русский'), ("O'zbekcha", "O'zbekcha")], max_length=50),
        ),
    ]
