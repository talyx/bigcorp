from . import views

from django.urls import path
from .webhooks import stripe_webhook

app_name = 'payment'

urlpatterns = [
    path('shipping/', views.shipping, name='shipping'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete-order/', views.complete_order, name='complete-order'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-failed/', views.payment_fail, name='payment-failed'),
    path('webhook-stripe/', stripe_webhook, name='webhook-stripe'),
    path('order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
    
]

