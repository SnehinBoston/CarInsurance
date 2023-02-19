from django.contrib import admin
from django.urls import path, include
from .views import payment_details, payment_success, create_test_payment, payment_failure

app_name="mypaymentapp"
urlpatterns = [
    path('payment-details/<int:payment_id>/', payment_details, name="payment_details"),
    path("payment-success/", payment_success),
    path(
        "payment-failure/",
        payment_failure,
    ),
    path("", create_test_payment, name="payment-page"),
]