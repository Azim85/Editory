# Generated by Django 3.2.2 on 2021-06-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymeuz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymetransactionmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]