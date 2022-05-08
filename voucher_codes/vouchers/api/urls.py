from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SpecialOfferViewSet, VoucherCodeCreate, VoucherCodeList, VoucherCodeDetail

router = DefaultRouter()
router.register('specialoffer', SpecialOfferViewSet, basename='specialoffer')

urlpatterns = [
    path('', include(router.urls)),

    path('<int:pk>/voucher_code-create/<int:user_pk>/', VoucherCodeCreate.as_view(), name='voucher-code-create'),
    path('<int:pk>/voucher_codes/', VoucherCodeList.as_view(), name='voucher-code-list'),
    path('voucher_code/<str:pk>/', VoucherCodeDetail.as_view(), name='voucher-code-detail'),
]