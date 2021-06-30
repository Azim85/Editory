# Generated by Django 3.2.2 on 2021-05-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0017_auto_20210525_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('material_name', models.CharField(max_length=255)),
                ('research_area', models.CharField(max_length=255)),
                ('choose', models.CharField(choices=[('стратегия исследования', 'стратегия исследования'), ('Научное сотрудничество', 'Научное сотрудничество'), ('Научное финансирование', 'Научное финансирование'), ('Управление и ведение', 'Управление и ведение')], max_length=100)),
                ('academic_degree', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('scientific_adviser', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('upload_file', models.FileField(upload_to='files/')),
                ('is_agree', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заказ рецензии на диссертацию',
                'verbose_name_plural': 'Заказ рецензии на диссертацию',
            },
        ),
    ]
