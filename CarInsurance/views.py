from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import CarInsuranceForm
from .models import CarInsurance
# import stripe
# stripe.api_key = 'sk_test_51Mboi8CmhlAp5PdFADmjoXevvTD1gArzDX0I99nd0ww0tIoyRIfi2HRefEkSAdEyAIFOWeaYZ9Pk0etnra6hLBoV00FymhBlrw'
# Create your views here.
class index(FormView):
    form_class = CarInsuranceForm
    template_name = 'index.html'
    success_url = reverse_lazy('mypaymentapp:payment-page')
    
    def get_initial(self):
        initial = super(index, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'name': self.request.user.get_full_name()})
        return initial

    def form_valid(self, form):
        # self.to_payments(form.cleaned_data)
        return super(index, self).form_valid(form)

    # def form_invalid(self, form):
    #     return ""
    # def to_payments(self, valid_data):
    #     print(valid_data)
    #     return HttpResponseRedirect(redirect_to='payments/')
    # if request.method == 'POST':
    #     form = CarInsuranceForm(request.POST)

    #     if form.is_valid():
    #         make = form.cleaned_data['make']
    #         model = form.cleaned_data['model']
    #         year = form.cleaned_data['year']
    #         mileage = form.cleaned_data['mileage']
    #         p = CarInsurance(make=make, model=model, year=year, mileage=mileage)
    #         p.save()

    #         return HttpResponseRedirect(redirect_to="/payments")
    
    # else:
    #     form = CarInsuranceForm()

    # context = {'form': form}
    # return render(request, 'index.html', context)


# form_class = ContactForm
#     template_name = 'contact-us.html'
#     success_url = reverse_lazy('<app-name>:contact-us')

#     def form_valid(self, form):
#         self.send_mail(form.cleaned_data)
#         return super(ContactView, self).form_valid(form)

#     def send_mail(self, valid_data):
#         # Send mail logic
#         print(valid_data)
#         pass
# YOUR_DOMAIN = 'http://localhost:4242'

# def create_checkout_session():
#     try:
#         checkout_session = stripe.checkout.Session.create(
#             line_items = [
#                 {
#                     'price': '{{PRICE_ID}}',
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
            
#         )
# def create_checkout_session():
#     try:
#         checkout_session = stripe.checkout.Session.create(
#             line_items=[
#                 {
#                     # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                     'price': '{{PRICE_ID}}',
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success.html',
#             cancel_url=YOUR_DOMAIN + '/cancel.html',
#         )
#     except Exception as e:
#         return str(e)

#     return redirect(checkout_session.url, code=303)
# class PaymentView(TemplateView):
#     template_name = "payment.html"
# def thanks(request):
#     return render(request, "CarInsurance/thanks.html")

    