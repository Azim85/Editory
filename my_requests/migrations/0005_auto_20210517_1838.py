# Generated by Django 3.2.2 on 2021-05-17 18:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0004_consultation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consultation',
            options={'verbose_name': 'консультация', 'verbose_name_plural': 'консультации'},
        ),
        migrations.AddField(
            model_name='consultation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]