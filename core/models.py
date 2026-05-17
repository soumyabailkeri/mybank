from django.db import models

class Transaction(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"

class TellerSession(models.Model):
    teller_name = models.CharField(max_length=100)
    cash_drawer_opening_balance = models.DecimalField(max_digits=10, decimal_places=2)
    cash_drawer_closing_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    session_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.teller_name} - {self.session_date}"
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.is_completed}"