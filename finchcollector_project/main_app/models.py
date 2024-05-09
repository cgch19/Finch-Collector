from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    colors = models.CharField(max_length=200)

    def __str__(self):
        return self.name

       