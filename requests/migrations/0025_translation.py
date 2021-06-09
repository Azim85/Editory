# Generated by Django 3.2.2 on 2021-06-08 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requests', '0024_auto_20210608_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_amount', models.IntegerField()),
                ('language', models.CharField(max_length=100)),
                ('research_area', models.CharField(choices=[('TEXT', 'TEXT'), ('TEXT', 'TEXT')], max_length=100)),
                ('extra', models.CharField(choices=[('TEXT', 'TEXT'), ('TEXT', 'TEXT')], max_length=100)),
                ('comment', models.TextField()),
                ('file', models.FileField(upload_to='files/')),
                ('is_agree', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
    ]
