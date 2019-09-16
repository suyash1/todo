from django.urls import path

from . import views

urlpatterns = [
    path('customer', views.CustomerAPI.as_view(), name='customer'),
    path('customer/<str:customer_id>', views.CustomerAPI.as_view(), name='get_customer_by_id'),
]