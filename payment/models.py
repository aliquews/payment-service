from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.TextField()
    price = models.IntegerField(null=False)

    def __str__(self) -> str:
        return f'{self.name} - {self.price}'