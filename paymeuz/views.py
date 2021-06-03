import base64
import time

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .keywords import *
from .models import PaymeTransactionModel
from .serializers import PaycomOperationSerialzer


class MerchantAPIView(APIView):
    http_method_names = ['post']
    authentication_classes = []
    VALIDATE_CLASS = None
    reply = None

    def __init__(self):
        self.METHODS = {
            METHOD_CHECK_PERFORM_TRANSACTION: self.check_perform_transaction,
            METHOD_CREATE_TRANSACTION: self.create_transaction,
            METHOD_PERFORM_TRANSACTION: self.perform_transaction,
            METHOD_CHECK_TRANSACTION: self.check_transaction,
            METHOD_CANCEL_TRANSACTION: self.cancel_transaction
        }
        self.REPLY_RESPONSE = {
            ORDER_FOUND: self.order_found,
            ORDER_NOT_FOUND: self.order_not_found,
            INVALID_AMOUNT: self.invalid_amount
        }
        super(MerchantAPIView, self).__init__()

    def post(self, request):
        header = request.META.get('HTTP_AUTHORIZATION')

        if header:
            hash_value = header.split()[-1]
            hash_value = hash_value.encode('utf-8')
            password = base64.b64decode(hash_value).decode('utf-8')
            password = password.split(':')[-1]

            if password == settings.PAYMEUZ_SETTINGS['KEY']:
                serializer = PaycomOperationSerialzer(data=request.data, many=False)
                serializer.is_valid(raise_exception=True)
                method = serializer.validated_data['method']
                self.METHODS[method](serializer.validated_data)

                assert self.reply is not None
                return Response(self.reply)

        error_data = {
            "error": {
                "code": AUTH_FAILED,
                "message": AUTH_FAILED_MESSAGE
            }
        }

        return Response(data=error_data, status=status.HTTP_200_OK)

    def check_perform_transaction(self, validated_data):
        assert self.VALIDATE_CLASS is not None
        result = self.VALIDATE_CLASS().check_order(amount=validated_data['params']['amount'],
                                                   order_id=validated_data['params']['account']['order_id'])
        assert result is not None
        self.REPLY_RESPONSE[result](validated_data)

    def create_transaction(self, validated_data):
        if PaymeTransactionModel.objects.filter(_id=validated_data['params']['id']).exists():
            obj = PaymeTransactionModel.objects.get(_id=validated_data['params']['id'])
            self.reply = dict(result=dict(
                create_time=obj.create_time,
                transaction=str(obj.id),
                state=CREATE_TRANSACTION
            ))
        elif PaymeTransactionModel.objects.filter(order_id=validated_data['params']['account']['order_id']).exists():
            self.reply = dict(error=dict(
                id=validated_data['id'],
                code=ORDER_BUSY,
                message=ORDER_BUSY_MESSAGE
            ))
        else:
            result = self.VALIDATE_CLASS().check_order(amount=validated_data['params']['amount'],
                                                       order_id=validated_data['params']['account']['order_id'])
            if result == ORDER_FOUND:
                create_time = int(time.time() * 1000)
                obj = PaymeTransactionModel.objects.create(
                    request_id=validated_data['id'],
                    _id=validated_data['params']['id'],
                    amount=validated_data['params']['amount'],
                    order_id=validated_data['params']['account']['order_id'],
                    state=CREATE_TRANSACTION,
                    create_time=create_time
                )
                self.reply = dict(result=dict(
                    create_time=create_time,
                    transaction=str(obj.id),
                    state=CREATE_TRANSACTION
                ))
            else:
                self.REPLY_RESPONSE[result](validated_data)

    def check_transaction(self, validated_data):
        try:
            obj = PaymeTransactionModel.objects.get(_id=validated_data['params']['id'])
            self.reply = dict(
                result=dict(
                    create_time=obj.create_time,
                    perform_time=obj.perform_time,
                    cancel_time=obj.cancel_time,
                    transaction=str(obj.id),
                    state=obj.state,
                    reason=obj.cancel_reason
                )
            )
        except PaymeTransactionModel.DoesNotExist:
            self.reply = dict(error=dict(
                id=validated_data['id'],
                code=TRANSACTION_NOT_FOUND,
                message=TRANSACTION_NOT_FOUND_MESSAGE
            ))

    def perform_transaction(self, validated_data):
        id = validated_data['params']['id']
        request_id = validated_data['id']
        try:
            obj = PaymeTransactionModel.objects.get(_id=id)
            if obj.state == CREATE_TRANSACTION:

                obj.state = CLOSE_TRANSACTION
                obj.status = SUCCESS

                perform_time = int(time.time() * 1000)

                obj.perform_time = perform_time
                obj.save()

                self.reply = dict(result=dict(
                    transaction=str(obj.id),
                    perform_time=perform_time,
                    state=CLOSE_TRANSACTION
                ))
            elif obj.state in [CANCEL_CREATE_TRANSACTION, CANCEL_CLOSE_TRANSACTION]:
                self.reply = dict(error=dict(
                    id=request_id,
                    code=UNABLE_TO_PERFORM_OPERATION,
                    message=UNABLE_TO_PERFORM_OPERATION_MESSAGE
                ))
            else:
                self.reply = dict(result=dict(
                    transaction=str(obj.id),
                    perform_time=obj.perform_time,
                    state=obj.state
                ))
        except PaymeTransactionModel.DoesNotExist:
            self.reply = dict(error=dict(
                id=request_id,
                code=TRANSACTION_NOT_FOUND,
                message=TRANSACTION_NOT_FOUND_MESSAGE
            ))

    def cancel_transaction(self, validated_data):
        id = validated_data['params']['id']
        request_id = validated_data['id']
        try:
            obj = PaymeTransactionModel.objects.get(_id=id)
            if obj.state == CLOSE_TRANSACTION:

                obj.state = CANCEL_CLOSE_TRANSACTION
                obj.status = CANCELED
                obj.cancel_reason = validated_data['params']['reason']

                cancel_time = int(time.time() * 1000)

                obj.cancel_time = cancel_time
                obj.save()

                self.reply = dict(result=dict(
                    transaction=str(obj.id),
                    cancel_time=cancel_time,
                    state=obj.state
                ))
            elif obj.state == CREATE_TRANSACTION:

                obj.state = CANCEL_CREATE_TRANSACTION
                obj.status = CANCELED
                obj.cancel_reason = validated_data['params']['reason']

                cancel_time = int(time.time() * 1000)

                obj.cancel_time = cancel_time
                obj.save()

                self.reply = dict(result=dict(
                    transaction=str(obj.id),
                    cancel_time=cancel_time,
                    state=obj.state
                ))
            else:
                self.reply = dict(result=dict(
                    transaction=str(obj.id),
                    cancel_time=obj.cancel_time,
                    state=obj.state
                ))
        except PaymeTransactionModel.DoesNotExist:
            self.reply = dict(error=dict(
                id=request_id,
                code=TRANSACTION_NOT_FOUND,
                message=TRANSACTION_NOT_FOUND_MESSAGE
            ))

    def order_found(self, validated_data):
        self.reply = dict(result=dict(allow=True))

    def order_not_found(self, validated_data):
        self.reply = dict(error=dict(
            id=validated_data['id'],
            code=ORDER_NOT_FOUND,
            message=ORDER_NOT_FOUND_MESSAGE
        ))

    def invalid_amount(self, validated_data):
        self.reply = dict(error=dict(
            id=validated_data['id'],
            code=INVALID_AMOUNT,
            message=INVALID_AMOUNT_MESSAGE
        ))
