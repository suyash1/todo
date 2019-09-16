from django.db import models
from customer.models import Customer


class Policy(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=10)
    premium = models.FloatField(default=0)
    cover = models.FloatField(default=0)

    class Meta:
        db_table = 'policy'

    def __str__(self):
        return 'Policy: ' + self.type
