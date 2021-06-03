from django.conf import settings
from django.utils.translation import ugettext_lazy as _

ORDER_NOT_FOUND = -31050
TRANSACTION_NOT_FOUND = -31003
UNABLE_TO_PERFORM_OPERATION = -31008
INVALID_AMOUNT = -31001
ORDER_FOUND = 200
AUTH_FAILED = -32504
ORDER_BUSY = -31050

CREATE_TRANSACTION = 1
CLOSE_TRANSACTION = 2
CANCEL_CREATE_TRANSACTION = -1
CANCEL_CLOSE_TRANSACTION = -2

AUTH_FAILED_MESSAGE = {
    "uz": "Authorization failed",
    "ru": "Authorization failed",
    "en": "Authorization failed"
}

ORDER_BUSY_MESSAGE = {
    "uz": "Order is occupied with other transaction",
    "ru": "Order is occupied with other transaction",
    "en": "Order is occupied with other transaction"
}

ORDER_NOT_FOUND_MESSAGE = {
    'uz': 'Buyurtma topilmadi',
    'ru': 'Заказ не найден',
    'en': 'Order not found'
}
TRANSACTION_NOT_FOUND_MESSAGE = {
    'uz': 'Tranzaksiya topilmadi',
    'ru': 'Транзакция не найдена',
    'en': 'Transaction not found'
}
UNABLE_TO_PERFORM_OPERATION_MESSAGE = {
    'uz': 'Ushbu amalni bajarib bo\'lmaydi',
    'ru': 'Невозможно выполнить данную операцию',
    'en': 'Unable to perform operation'
}
INVALID_AMOUNT_MESSAGE = {
    'uz': 'Miqdori notog\'ri',
    'ru': 'Неверная сумма',
    'en': 'Invalid amount'
}

PROCESSING = 'processing'
SUCCESS = 'success'
FAILED = 'failed'
CANCELED = 'canceled'

PAYME_PAYMENT_STATUS = (
    (PROCESSING, _('processing')),
    (SUCCESS, _('success')),
    (FAILED, _('failed')),
    (CANCELED, _('canceled')),
)

assert settings.PAYMEUZ_SETTINGS.get('TEST_ENV') is not None
assert settings.PAYMEUZ_SETTINGS.get('ID') is not None
assert settings.PAYMEUZ_SETTINGS.get('ACCOUNTS') is not None
assert settings.PAYMEUZ_SETTINGS['ACCOUNTS'].get('KEY_1') is not None

TEST_ENV = settings.PAYMEUZ_SETTINGS['TEST_ENV']
TOKEN = settings.PAYMEUZ_SETTINGS['ID']
AUTHORIZATION = {'X-Auth': settings.PAYMEUZ_SETTINGS['ID']}
KEY_1 = settings.PAYMEUZ_SETTINGS['ACCOUNTS']['KEY_1']
KEY_2 = settings.PAYMEUZ_SETTINGS['ACCOUNTS'].get('KEY_2', 'order_type')
ACCOUNTS = settings.PAYMEUZ_SETTINGS['ACCOUNTS']

RECEIPTS_CREATE = 'receipts.create'
RECEIPTS_PAY = 'receipts.pay'
CARDS_CREATE = 'cards.create'
CARDS_GET_VERIFY_CODE = 'cards.get_verify_code'
CARD_VERIFY = 'cards.verify'

TEST_URL = 'https://checkout.test.paycom.uz/api'
PRODUCTION_URL = 'https://checkout.paycom.uz/api'
INITIALIZATION_URL = 'https://checkout.paycom.uz'
TEST_INITIALIZATION_URL = 'https://checkout.test.paycom.uz'
URL = PRODUCTION_URL if TEST_ENV else TEST_URL
LINK = INITIALIZATION_URL if TEST_ENV else TEST_INITIALIZATION_URL

METHOD_CHECK_PERFORM_TRANSACTION = 'CheckPerformTransaction'
METHOD_CREATE_TRANSACTION = 'CreateTransaction'
METHOD_CHECK_TRANSACTION = 'CheckTransaction'
METHOD_PERFORM_TRANSACTION = 'PerformTransaction'
METHOD_CANCEL_TRANSACTION = 'CancelTransaction'
