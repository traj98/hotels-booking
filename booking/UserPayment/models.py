from django.db import models

class UserPaymentdb(models.Model):
    payment_id = models.IntegerField()
    order_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    order_amt = models.IntegerField()
    product_info = models.CharField(max_length=1000)
    is_paid = models.BooleanField() 