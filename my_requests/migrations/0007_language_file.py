# Generated by Django 3.2.2 on 2021-07-30 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0006_alter_getpatent_application_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
