# Generated by Django 3.2.2 on 2021-07-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setpage', '0017_proofmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='LangEditModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField(blank=True)),
                ('text1_ru', models.TextField(blank=True, null=True)),
                ('text1_en', models.TextField(blank=True, null=True)),
                ('text1_uz', models.TextField(blank=True, null=True)),
                ('text2', models.TextField(blank=True)),
                ('text2_ru', models.TextField(blank=True, null=True)),
                ('text2_en', models.TextField(blank=True, null=True)),
                ('text2_uz', models.TextField(blank=True, null=True)),
                ('text3', models.CharField(blank=True, max_length=100)),
                ('text3_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text3_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text3_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text4', models.CharField(blank=True, max_length=100)),
                ('text5', models.CharField(blank=True, max_length=100)),
                ('text5_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text5_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text5_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text6', models.CharField(blank=True, max_length=100)),
                ('text7', models.CharField(blank=True, max_length=100)),
                ('text7_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text7_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text7_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text8', models.CharField(blank=True, max_length=100)),
                ('text9', models.CharField(blank=True, max_length=100)),
                ('text9_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text9_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text9_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text10', models.CharField(blank=True, max_length=100)),
                ('text10_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text10_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text10_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text11', models.CharField(blank=True, max_length=100)),
                ('text11_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text11_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text11_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text12', models.CharField(blank=True, max_length=100)),
                ('text12_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text12_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text12_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text13', models.CharField(blank=True, max_length=100)),
                ('text13_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text13_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text13_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text14', models.CharField(blank=True, max_length=100)),
                ('text14_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text14_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text14_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text15', models.CharField(blank=True, max_length=100)),
                ('text15_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text15_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text15_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text16', models.CharField(blank=True, max_length=100)),
                ('text16_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text16_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text16_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text17', models.CharField(blank=True, max_length=100)),
                ('text17_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text17_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text17_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text18', models.CharField(blank=True, max_length=100)),
                ('text18_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text18_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text18_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text19', models.CharField(blank=True, max_length=100)),
                ('text19_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text19_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text19_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text20', models.CharField(blank=True, max_length=100)),
                ('text20_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text20_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text20_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text21', models.CharField(blank=True, max_length=100)),
                ('text21_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text21_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text21_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text22', models.CharField(blank=True, max_length=100)),
                ('text22_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text22_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text22_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text23', models.CharField(blank=True, max_length=100)),
                ('text23_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text23_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text23_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('text24', models.CharField(blank=True, max_length=100)),
                ('text24_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('text24_en', models.CharField(blank=True, max_length=100, null=True)),
                ('text24_uz', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
