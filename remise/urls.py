from django.urls import path, include
from rest_framework.routers import DefaultRouter
from remise import views

router = DefaultRouter()
router.register(r"discounts", views.DiscountViewSet)
router.register(r"loyalty-points", views.LoyaltyPointViewSet)
router.register(r"loyalty-programs", views.LoyaltyProgramViewSet)
router.register(r"used-discounts", views.UsedDiscountViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
