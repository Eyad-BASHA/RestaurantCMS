import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from remise.models import Discount
from restaurant.models.order import Order


def order_total_amount(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        return JsonResponse({"total_amount": order.total_amount})
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)


def calculate_payment_amount(request):
    discount_id = request.GET.get("discount_id")
    order_id = request.GET.get("order_id")

    order = Order.objects.get(id=order_id)
    discount = Discount.objects.get(id=discount_id) if discount_id else None

    amount = order.total_amount
    if discount:
        if discount.discount_type == "percentage":
            amount -= amount * (discount.value / 100)
        elif discount.discount_type == "fixed":
            amount -= discount.value

    amount = round(max(amount, 0), 2)
    return JsonResponse({"amount": amount})


@csrf_exempt
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": "Order Name",
                    },
                    "unit_amount": 2000,  # Amount in cents
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url="https://yourdomain.com/success/",
        cancel_url="https://yourdomain.com/cancel/",
    )
    return JsonResponse({"id": session.id})
