from django.contrib import admin
from .models import Policy, CustomerPolicy


class PolicyAdmin(admin.ModelAdmin):
    list_display = ['policy_type', 'premium', 'cover', 'created_at', 'updated_at', 'is_disabled']
    search_fields = ['policy_type']
    list_filter = ['policy_type']
    ordering = ('policy_type', 'created_at', 'updated_at')


class CustomerPolicyAdmin(admin.ModelAdmin):
    list_display = ['customer', 'policy', 'created_at', 'updated_at', 'is_disabled']
    search_fields = ['customer', 'policy']
    ordering = ('created_at', 'updated_at')


admin.site.register(Policy, PolicyAdmin)
admin.site.register(CustomerPolicy, CustomerPolicyAdmin)
