from django.urls import path
from .views import index, TemplateView
app_name='CarInsurance'
urlpatterns = [
    path('', index.as_view(), name="index")
    # path('payment/', TemplateView.as_view(template_name = 'car_payment.html'), name="payment")
]