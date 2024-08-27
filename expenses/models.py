from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User
        

class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Category = models.CharField(default="category", max_length=50)
    date_added = models.DateTimeField(default=django.utils.timezone.now)
    grand_total = models.FloatField(default=0)
    description = models.TextField(default="description")

    class Meta:
        db_table = 'Expenses'

    def __str__(self) -> str:
        return "Expenses ID: " + str(self.Category) + " | Grand Total: " + str(self.grand_total) + " | Datetime: " + str(self.date_added)
    
    
    
