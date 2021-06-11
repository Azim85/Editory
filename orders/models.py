from django.db import models
from django.db.models.signals import pre_save

from users.models import CustomUser
# from books.models import BookModel
from django.utils.translation import ugettext_lazy as _

# Test

PAYMENT_TYPES = (
    (1, _('Наличные')),
    (2, _('Пластиковая карта')),
    (3, _('Apelsin')),
    (4, _('Payme')),
)

PAYMENT_STATUS = (
    (0, _('обрабатывается...')),
    (1, _('В ожидании')),
    (2, _('Ошибка')),
    (3, _('Завершено')),
    (4, _('Отменен')),
    (5, _('Истёк')),
    (6, _('Возвращен')),
)

DELIVERY_STATUS = (
    (1, _('В ожидании')),
    (2, _('На доставке')),
    (3, _('Доставлен')),
    (4, _('Возвращен')),
)


class OrderModel(models.Model):
    # books = models.ManyToManyField(BookModel, related_name='orders', verbose_name=_('books'))
    product = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(CustomUser, related_name='orders', verbose_name=_('user'), on_delete=models.CASCADE,
                             null=True, blank=True)
    amount = models.FloatField(verbose_name=_('amount'), null=True)
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    # fio = models.CharField(max_length=255, verbose_name=_('fio'))
    email = models.EmailField(verbose_name=_('email'))
    file = models.FileField(upload_to='files', null=True, blank=True)
    # city = models.CharField(max_length=255, verbose_name=_('city'), null=True, blank=True)
    # region = models.CharField(max_length=255, verbose_name=_('region'), null=True, blank=True)
    # street = models.CharField(max_length=255, verbose_name=_('street'), null=True, blank=True)
    # house = models.CharField(max_length=255, verbose_name=_('house'), null=True, blank=True)
    # full_address = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('full address'))
    # comment = models.TextField(null=True, blank=True, verbose_name=_('comment'))

    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_TYPES, verbose_name=_('type'))
    payment_status = models.PositiveSmallIntegerField(choices=PAYMENT_STATUS, verbose_name=_('status'), default=1)
    delivery_status = models.PositiveSmallIntegerField(choices=DELIVERY_STATUS, verbose_name=_('delivery status'), default=1)

    # source = models.CharField(max_length=255, verbose_name=_('source'), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_payme_amount(self):
        return self.amount * 100

    # def get_books_list(self):
    #     books_str = ', '.join([i.title for i in self.books.all()])
    #     return books_str

    def __str__(self):
        return self.email
        # return _('Order #') + str(self.pk)

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')


# def order_name_pre_save(sender, instance, signal, *args, **kwargs):
#     if instance.product == '':
#         instance.product = 'consultation'
#     instance.save()

# post_save.connect(order_name_pre_save, sender=PaymeTransactionModel, dispatch_uid='update_order_status_payme')