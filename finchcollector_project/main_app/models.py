from django.db import models
from django.utils import timezone

class Finch(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    colors = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Feeding(models.Model):
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    food_type = models.CharField(max_length=100)
    food_amount = models.CharField(max_length=100)

    def __str__(self):
        return f"Feeding for {self.finch.name} on {self.date}"
       