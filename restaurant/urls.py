from django.urls import path
from .views import calculate_payment_amount, order_total_amount

urlpatterns = [
    path(
        "orders/<int:order_id>/total_amount/",
        order_total_amount,
        name="order_total_amount",
    ),

    path(
        'calculate-payment-amount/', 
        calculate_payment_amount, 
        name='calculate_payment_amount'
        ),

]
