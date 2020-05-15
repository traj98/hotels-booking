from django.db import models

class EventBookingdb(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    age=models.IntegerField()
    proof=models.CharField(max_length=100)
    event=models.CharField(max_length=100)
    preferences=models.TextField(max_length=1000)

    def __str__(self):
        return self.username
