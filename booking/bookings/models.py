from django.db import models


class Bookingdb(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    age=models.IntegerField()
    proof=models.CharField(max_length=100)
    room_number=models.IntegerField()
    start_booking=models.DateField()
    end_booking=models.DateField()
    preferences=models.CharField(max_length=1000)

    def __str__(self):
        return self.username
