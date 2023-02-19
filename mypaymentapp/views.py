from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded
from .forms import TestPaymentForm

def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)

    try:
        form = payment.get_form(data = request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))

    return TemplateResponse(
        request,
        'payment.html',
        {'form': form, 'payment': payment}
    )

def payment_success(request):
    return HttpResponse("Payment succeeded.")

def payment_failure(request):
    return HttpResponse("Payment failed.")

def create_test_payment(request):
    form = TestPaymentForm(
        initial={"variant": "authorizenet", "currency": "USD", "total": 125.0},
        data = request.POST or None
    )
    if request.method == 'POST' and form.is_valid():
        p = form.instance
        p.description = "Car Insurance"
        
        p.save()
        return redirect(f"payment-details/{p.id}")
    return TemplateResponse(request, "create_payment.html", {"form": form})
