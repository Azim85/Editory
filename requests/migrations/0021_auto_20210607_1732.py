# Generated by Django 3.2.2 on 2021-06-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0020_auto_20210607_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationforfreeconsultation',
            options={'verbose_name': 'Participation in Conference', 'verbose_name_plural': 'Participation in Conference'},
        ),
        migrations.AddField(
            model_name='applicationforfreeconsultation',
            name='is_agree',
            field=models.BooleanField(default=False),
        ),
    ]
