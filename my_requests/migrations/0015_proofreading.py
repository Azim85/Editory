# Generated by Django 3.2.2 on 2021-05-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0014_alter_organizeresearches_is_agree'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proofreading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('material_name', models.CharField(max_length=255)),
                ('research_area', models.CharField(max_length=255)),
                ('choose', models.CharField(choices=[('стратегия исследования', 'стратегия исследования'), ('Научное сотрудничество', 'Научное сотрудничество'), ('Научное финансирование', 'Научное финансирование'), ('Управление и ведение', 'Управление и ведение')], max_length=100)),
                ('word_count', models.CharField(max_length=100)),
                ('language_editing', models.CharField(max_length=50)),
                ('certificate', models.TextField()),
                ('comment', models.TextField()),
                ('upload_file', models.FileField(upload_to='files/')),
            ],
            options={
                'verbose_name': 'Заявка на корректуру',
                'verbose_name_plural': 'Заявки на корректуру',
            },
        ),
    ]
