from django.db import models
from django.shortcuts import redirect

from decimal import Decimal
from payments import PurchasedItem
from payments.models import BasePayment

class Payment(BasePayment):
    def get_failure_url(self):
        return "http://localhost:8000/payments/payment-failure"
    
    def get_success_url(self):
        return "http://localhost:8000/payments/payment-success"

    def get_purchased_items(self):
        yield PurchasedItem(
            name = "Car Insurance",
            sku = 'CI',
            quantity = 1,
            price = Decimal(125),
            currency = "USD"
        )

