from django.urls import path

from .views import CreateSellerView, CreateChargeRecordView


urlpatterns = [
    path('add_seller/', CreateSellerView.as_view()),
    path('charge_account/', CreateChargeRecordView.as_view()),
]
