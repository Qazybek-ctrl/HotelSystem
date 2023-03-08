from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=5, )
    price = models.FloatField(default=1000.00)
    seat = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    start_day = models.DateField(auto_now=False, auto_now_add=False)
    end_day = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f'{self.user.username} for: {self.room.name}'
    