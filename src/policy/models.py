from django.db import models
from customer.models import Customer


class Policy(models.Model):
    policy_type = models.CharField(max_length=100)
    premium = models.FloatField(default=0)
    cover = models.FloatField(default=0)
    is_disabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'policy'
        ordering = ['-id']

    def __str__(self):
        return 'Policy: ' + self.policy_type


class CustomerPolicy(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    policy = models.ForeignKey(Policy, on_delete=models.DO_NOTHING)
    is_disabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customer_policy'
        ordering = ['-id']

    def __str__(self):
        return '%s-%s' % (self.customer, self.policy)
