from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True)
    due_date = models.DateField(null=True)

    class Meta:
        db_table = 'user_task'
        ordering = ['-id']
