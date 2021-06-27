from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import ExPrice

router = DefaultRouter()
router.register(r'v1/generate-address', GenerateAddressViewset, basename='GenerateAddressViewset')
router.register(r'v1/details-by-address', GetDetailByAddressViewset, basename='GetDetailByAddressViewset')
router.register(r'v1/transcation-details-by-address', GetTransactionByAddressViewset, basename='GetTransactionByAddressViewset')
router.register(r'v1/exchange-rate',GetTransactionFeeViewset,basename='GetTransactionFeeViewset')
# router.register(r'v1/exchange-price', ExPrice.as_view(), basename='ListWalletPriceViewset')

urlpatterns = [
    path('', include(router.urls)),
    url(r'v1/exchange-price', ExPrice.as_view())
]