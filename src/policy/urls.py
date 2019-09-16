from django.urls import path

from . import views

urlpatterns = [
    path('policy', views.PolicyAPI.as_view(), name='policy'),
    path('policy/<str:policy_id>', views.PolicyAPI.as_view(), name='get_policy_by_id'),
    path('policy_subscription', views.CustomerPolicyAPI.as_view(), name='subscription'),
    path('policy_subscription/<str:subscription_id>', views.CustomerPolicyAPI.as_view(), 
        name='get_subscription_by_id'),
]