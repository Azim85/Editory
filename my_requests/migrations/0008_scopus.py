# Generated by Django 3.2.2 on 2021-07-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0007_baks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scopus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('organization', models.CharField(max_length=255)),
                ('org_contacts', models.CharField(max_length=255)),
                ('org_address', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True, null=True)),
                ('is_agree', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Scopus',
                'verbose_name_plural': 'Scopus requests',
            },
        ),
    ]
