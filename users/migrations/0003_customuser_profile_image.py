# Generated by Django 3.2.2 on 2021-05-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(default='no profile image', upload_to='profile_images/'),
        ),
    ]
