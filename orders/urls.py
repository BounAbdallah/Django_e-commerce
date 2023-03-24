from django.urls import path
from orders.views import Order_create, Order_created
urlpatterns = [
    path("checkout/", Order_create, name="Order_create"),
    path("thanks/", Order_created, name="Order_created"),
]
