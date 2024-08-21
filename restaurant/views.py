from django.http import JsonResponse
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

    # Arrondir le montant à deux chiffres après la virgule
    amount = round(max(amount, 0), 2)

    return JsonResponse({"amount": amount})
