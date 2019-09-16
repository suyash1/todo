from django.contrib import admin
from .models import Policy


class PolicyAdmin(admin.ModelAdmin):
    list_display = ['customer', 'type', 'premium', 'cover']
    search_fields = ['customer__first_name', 'customer__last_name', 'type']
    list_filter = ['customer', 'type']
    ordering = ('customer', 'type')


admin.site.register(Policy, PolicyAdmin)
