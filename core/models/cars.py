from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=150 , blank=False , null=False)
    model = models.CharField(max_length=150 , blank=False , null=False)
    year = models.IntegerField(max_length=4 , blank=False , null=False)
    price = models.IntegerField(max_length=10 , blank=False , null=False)
    color = models.CharField(max_length=50 , blank=False , null=False)

    def __str__(self):
        return f'{self.name} {self.model}'