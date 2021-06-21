# Generated by Django 3.2.2 on 2021-06-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_requests', '0022_auto_20210607_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('organization', models.CharField(max_length=255)),
                ('org_contacts', models.CharField(max_length=255)),
                ('org_address', models.CharField(max_length=255)),
                ('is_agree', models.BooleanField(default=False)),
                ('theme', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Grant',
                'verbose_name_plural': 'Grants',
            },
        ),
        migrations.AlterModelOptions(
            name='organizeconferences',
            options={'verbose_name': 'Create Conference', 'verbose_name_plural': 'Crete Conferences'},
        ),
    ]