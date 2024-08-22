from django.urls import path

from .views import *

urlpatterns = [
    # Product URLs
    path("products/", ProductListCreateView.as_view(), name="product-list-create"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    # Stock Location URLs
    path(
        "locations/", StockLocationListCreateView.as_view(), name="location-list-create"
    ),
    path(
        "locations/<int:pk>/", StockLocationDetailView.as_view(), name="location-detail"
    ),
    # Stock Movement URLs
    path(
        "movements/", StockMovementListCreateView.as_view(), name="movement-list-create"
    ),
    path(
        "movements/<int:pk>/", StockMovementDetailView.as_view(), name="movement-detail"
    ),
]
