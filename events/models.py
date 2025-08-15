from django.db import models
from epic.models import User
from django.contrib.auth import get_user_model

# User = get_user_model()
# class Price(models.model):
#     price = models.FloatField
    
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    total_tickets = models.PositiveIntegerField()
    available_tickets = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name} x total-cost:#{self.quantity*self.event.price}"