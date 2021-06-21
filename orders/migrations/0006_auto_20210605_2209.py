# Generated by Django 3.2.2 on 2021-06-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_ordermodel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='payment_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'обрабатывается...'), (1, 'В ожидании'), (2, 'Ошибка'), (3, 'Завершено'), (4, 'Отменен'), (5, 'Истёк'), (6, 'Возвращен')], default=1, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='payment_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Наличные'), (2, 'Пластиковая карта'), (3, 'Apelsin'), (4, 'Payme')], verbose_name='type'),
        ),
    ]