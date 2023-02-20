from django.urls import path

from views import CreateSellerView


urlpatterns = [
    path('add_seller/', CreateSellerView.as_view())
]
