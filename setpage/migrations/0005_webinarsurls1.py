# Generated by Django 3.2.2 on 2021-08-10 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setpage', '0004_top10_top10uz_top25_top5uz'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebinarsUrls1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=225)),
            ],
        ),
    ]
