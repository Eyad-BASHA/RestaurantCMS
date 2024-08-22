from django.urls import path
from restaurant.views import (
    calculate_payment_amount,
    order_total_amount,
    create_checkout_session,
)
from .res_views.order import *
from .res_views.payment.PaymentViews import *
from .res_views.reservation import *
from .res_views.restaurant import *

urlpatterns = [
    # Calculer le montant total d'une commande
    path(
        "orders/<int:order_id>/total_amount/",
        order_total_amount,
        name="order_total_amount",
    ),
    path(
        "calculate-payment-amount/",
        calculate_payment_amount,
        name="calculate_payment_amount",
    ),
    # Gestion des commandes
    path("orders/create/", CreateOrderView.as_view(), name="create-order"),
    path(
        "orders/create-for-client/",
        CreateOrderForClientView.as_view(),
        name="create-order-for-client",
    ),
    path(
        "orders/my-orders/", ListClientOrdersView.as_view(), name="list-client-orders"
    ),
    path(
        "orders/restaurant-orders/",
        ListRestaurantOrdersView.as_view(),
        name="list-restaurant-orders",
    ),
    path("orders/<int:pk>/update/", UpdateOrderView.as_view(), name="update-order"),
    # Gestion des paiements
    path("orders/stripe-payment/", StripePaymentView.as_view(), name="stripe-payment"),
    path("orders/record-payment/", RecordPaymentView.as_view(), name="record-payment"),
    path("orders/split-payment/", SplitPaymentView.as_view(), name="split-payment"),
    # Méthodes de paiement
    path(
        "payment-methods/",
        PaymentMethodListCreateView.as_view(),
        name="payment-method-list-create",
    ),
    path(
        "payment-methods/<int:pk>/",
        PaymentMethodDetailView.as_view(),
        name="payment-method-detail",
    ),
    # Paiements
    path("payments/", PaymentListView.as_view(), name="payment-list"),
    path("payments/create/", PaymentCreateView.as_view(), name="payment-create"),
    path("payments/<int:pk>/", PaymentDetailView.as_view(), name="payment-detail"),
    # Checkout session avec Stripe
    path("payments/stripe/", create_checkout_session, name="stripe-payment"),
    # URLs pour les réservations
    path(
        "reservations/",
        ReservationListCreateView.as_view(),
        name="reservation-list-create",
    ),
    path(
        "reservations/<int:pk>/",
        ReservationDetailView.as_view(),
        name="reservation-detail",
    ),
    # URLs pour les disponibilités
    path(
        "availabilities/",
        AvailabilityListCreateView.as_view(),
        name="availability-list-create",
    ),
    path(
        "availabilities/<int:pk>/",
        AvailabilityDetailView.as_view(),
        name="availability-detail",
    ),
    # Restaurant URLs
    path(
        "restaurants/",
        RestaurantListCreateView.as_view(),
        name="restaurant-list-create",
    ),
    path(
        "restaurants/<int:pk>/",
        RestaurantDetailView.as_view(),
        name="restaurant-detail",
    ),
    # Address URLs
    path(
        "addresses/",
        AddressRestaurantListCreateView.as_view(),
        name="address-list-create",
    ),
    path(
        "addresses/<int:pk>/",
        AddressRestaurantDetailView.as_view(),
        name="address-detail",
    ),
    # Menu URLs
    path("menus/", MenuListCreateView.as_view(), name="menu-list-create"),
    path("menus/<int:pk>/", MenuDetailView.as_view(), name="menu-detail"),
    path("menu-items/", MenuItemListCreateView.as_view(), name="menuitem-list-create"),
    path("menu-items/<int:pk>/", MenuItemDetailView.as_view(), name="menuitem-detail"),
    path(
        "type-menu-items/",
        TypeMenuItemListCreateView.as_view(),
        name="type-menuitem-list-create",
    ),
    path(
        "type-menu-items/<int:pk>/",
        TypeMenuItemDetailView.as_view(),
        name="type-menuitem-detail",
    ),
    path(
        "category-menu-items/",
        CategoryMenuItemListCreateView.as_view(),
        name="category-menuitem-list-create",
    ),
    path(
        "category-menu-items/<int:pk>/",
        CategoryMenuItemDetailView.as_view(),
        name="category-menuitem-detail",
    ),
    path(
        "category-restaurants/",
        CategoryRestaurantListCreateView.as_view(),
        name="category-restaurant-list-create",
    ),
    path(
        "category-restaurants/<int:pk>/",
        CategoryRestaurantDetailView.as_view(),
        name="category-restaurant-detail",
    ),
    # Photo URLs
    path(
        "menu-photos/",
        PhotoMenuItemListCreateView.as_view(),
        name="menuphoto-list-create",
    ),
    path(
        "menu-photos/<int:pk>/",
        PhotoMenuItemDetailView.as_view(),
        name="menuphoto-detail",
    ),
    # Review URLs
    path("reviews/", ReviewListCreateView.as_view(), name="review-list-create"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
]
