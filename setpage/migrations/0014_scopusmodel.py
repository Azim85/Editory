# Generated by Django 3.2.2 on 2021-07-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setpage', '0013_patentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScopusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(blank=True, max_length=255)),
                ('text1_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('text1_en', models.CharField(blank=True, max_length=255, null=True)),
                ('text1_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('text2', models.TextField(blank=True, max_length=255)),
                ('text2_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('text2_en', models.TextField(blank=True, max_length=255, null=True)),
                ('text2_uz', models.TextField(blank=True, max_length=255, null=True)),
                ('text3', models.CharField(blank=True, max_length=255)),
                ('text3_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('text3_en', models.CharField(blank=True, max_length=255, null=True)),
                ('text3_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('text4', models.ImageField(blank=True, upload_to='pages/')),
                ('text5', models.TextField(blank=True, max_length=255)),
                ('text5_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('text5_en', models.TextField(blank=True, max_length=255, null=True)),
                ('text5_uz', models.TextField(blank=True, max_length=255, null=True)),
                ('text6', models.ImageField(blank=True, upload_to='pages/')),
                ('text7', models.TextField(blank=True, max_length=255)),
                ('text7_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('text7_en', models.TextField(blank=True, max_length=255, null=True)),
                ('text7_uz', models.TextField(blank=True, max_length=255, null=True)),
                ('text8', models.ImageField(blank=True, upload_to='pages/')),
                ('text9', models.TextField(blank=True, max_length=255)),
                ('text9_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('text9_en', models.TextField(blank=True, max_length=255, null=True)),
                ('text9_uz', models.TextField(blank=True, max_length=255, null=True)),
                ('text10', models.TextField(blank=True, max_length=255)),
                ('text10_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('text10_en', models.TextField(blank=True, max_length=255, null=True)),
                ('text10_uz', models.TextField(blank=True, max_length=255, null=True)),
                ('text11', models.TextField(blank=True, max_length=255)),
                ('text11_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('text11_en', models.TextField(blank=True, max_length=255, null=True)),
                ('text11_uz', models.TextField(blank=True, max_length=255, null=True)),
                ('text12', models.TextField(blank=True, max_length=255)),
                ('text12_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('text12_en', models.TextField(blank=True, max_length=255, null=True)),
                ('text12_uz', models.TextField(blank=True, max_length=255, null=True)),
                ('text13', models.TextField(blank=True, max_length=255)),
                ('text13_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('text13_en', models.TextField(blank=True, max_length=255, null=True)),
                ('text13_uz', models.TextField(blank=True, max_length=255, null=True)),
                ('text14', models.TextField(blank=True, max_length=255)),
                ('text14_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('text14_en', models.TextField(blank=True, max_length=255, null=True)),
                ('text14_uz', models.TextField(blank=True, max_length=255, null=True)),
                ('text15', models.TextField(blank=True, max_length=255)),
                ('text15_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('text15_en', models.TextField(blank=True, max_length=255, null=True)),
                ('text15_uz', models.TextField(blank=True, max_length=255, null=True)),
                ('text16', models.TextField(blank=True, max_length=255)),
                ('text16_ru', models.TextField(blank=True, max_length=255, null=True)),
                ('text16_en', models.TextField(blank=True, max_length=255, null=True)),
                ('text16_uz', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]