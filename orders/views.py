from datetime import datetime
from .forms import OrderForm
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect, render

# from clickuz import ClickUz
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
# from openpyxl import Workbook
from rest_framework.views import APIView

from orders.models import OrderModel
from paymeuz.methods import Paymeuz
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.response import Response

from orders.serializers import OrderCreateSerializer


class OrderCreateView(CreateAPIView):
    serializer_class = OrderCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        if obj.payment_type not in (1, 2):
            url = ''
            # if obj.payment_type == 3:
            #     url = ClickUz.generate_url(order_id=obj.id,
            #                                amount=obj.amount,
            #                                return_url='http://in-study.uz/success')
            if obj.payment_type == 4:
                url = Paymeuz.create_initialization(amount=obj.amount * 100,
                                                    order_id=str(obj.id),


                return_url='https://01bd51aace4b.ngrok.io/success')


            return Response({'redirect_url': url}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderCancelView(APIView):

    def post(self, request, *args, **kwargs):
        order = get_object_or_404(OrderModel,
                                  pk=self.kwargs['pk'],
                                  user=self.request.user)

        if order.payment_type in (1, 2):
            if order.payment_status == 1:
                order.payment_status = 4
                order.save()
                return Response({'status': True})
        return Response({'status': False})


@user_passes_test(lambda u: u.is_superuser)
def order_export(request):
    orders = OrderModel.objects.all()

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename={date}-отчет.xlsx'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )
    workbook = Workbook()

    # Get active worksheet/tab
    worksheet = workbook.active
    worksheet.title = 'Orders'

    # Define the titles for columns
    columns = [
        'Order #',
        'Customer name',
        'Phone',
        'Book title',
        'Author',
        'Cover type',
        'Amount',
        'Payment type',
        'Supplier',
        'Performed by',
    ]
    row_num = 1

    # Assign the titles for each cell of the header
    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    # Iterate through all movies
    for order in orders:
        for book in order.books.all():
            row_num += 1

            # Define the data for each cell in the row
            row = [
                order.id,
                order.user.profile.fio,
                order.user.profile.phone,
                book.title,
                book.author.name,
                book.get_book_type_display(),
                book.current_price,
                order.get_payment_type_display(),
                book.supplier.title,
                order.fio
            ]

            # Assign the data for each cell of the row
            for col_num, cell_value in enumerate(row, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = cell_value

    workbook.save(response)

    return response



class CreateOrderView(View):
    def post(self, request):
        user = request.user
        product = request.POST.get('product')
        amount = request.POST.get('amount')
        payment_type = request.POST.get('payment_type')
        payment_status = request.POST.get('payment_status')
        delivery_status = request.POST.get('delivery_status')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.FILES.get('file')
        print(request.POST.get('product'))

        done = OrderModel.objects.create(user=user, product=product, amount=amount, payment_type=payment_type, payment_status=payment_status, delivery_status=delivery_status, email=email, phone=phone, file=file )
        if done:
            return redirect('orders:choose-type')

        return redirect('pages:language_editing')

class ChooseTypeView(View):
    def get(self, request):
        order = OrderModel.objects.first()
        return render(request, 'payment_type.html', {'order':order})

class TransPaymentView(View):
    def get(self, request):
        order = OrderModel.objects.first()
        return render(request, 'translation_payment.html', {'order':order})

class ChangePaymentTypeView(View):
    def post(self, request):
        order = OrderModel.objects.first()
        order.payment_type = request.POST.get('payment-type')
        order.save()
        order.refresh_from_db()
        return redirect('orders:translation-payment')
            # return render(request, 'translation_payment.html', {'order':order})
        # return render(request, 'translation_payment.html', {'order':order})
    