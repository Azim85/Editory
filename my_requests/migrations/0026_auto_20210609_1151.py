# Generated by Django 3.2.2 on 2021-06-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0025_translation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getpatent',
            name='application_upload',
            field=models.FileField(upload_to='app_requests/'),
        ),
        migrations.AlterField(
            model_name='publicationtoscopus',
            name='application_upload',
            field=models.FileField(upload_to='app_requests/'),
        ),
        migrations.AlterField(
            model_name='researchgrant',
            name='application_upload',
            field=models.FileField(upload_to='app_requests/'),
        ),
    ]