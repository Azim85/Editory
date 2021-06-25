from django.db.models import Q
from django.http import Http404
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

# from books.models import BookModel
# from books.serializers import BookListSerializer
from orders.models import OrderModel


class OrderCreateSerializer(serializers.ModelSerializer):
    books = serializers.CharField()

    def create(self, validated_data):
        books = validated_data.pop('books')
        user = self.context['user']

        order = super().create(validated_data)
        amount = 0

        for book in books.split(','):
            obj = get_object_or_404(BookModel, pk=book, is_active=True)
            # if not obj.bought(user):
            amount += obj.current_price
            order.books.add(obj)

        if amount == 0:
            print(books)
            raise Http404

        order.amount = amount
        order.user = user
        order.save()

        return order

    class Meta:
        model = OrderModel
        exclude = ['payment_status', 'amount']


class ProfileOrdersListSerializer(serializers.ModelSerializer):
    # books = BookListSerializer(many=True)
    payment_type = serializers.SerializerMethodField()
    payment_status = serializers.SerializerMethodField()
    can_cancel = serializers.SerializerMethodField()

    def get_can_cancel(self, obj: OrderModel) -> bool:
        if obj.payment_type in (1, 2):
            if obj.payment_status == 1:
                return True
        return False

    def get_payment_type(self, obj):
        return obj.get_payment_type_display()

    def get_payment_status(self, obj):
        return obj.get_payment_status_display()

    class Meta:
        model = OrderModel
        fields = ['id', 'books', 'amount', 'created_at', 'payment_type', 'payment_status', 'can_cancel']
