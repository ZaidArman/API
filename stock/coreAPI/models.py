from django.db import models

# Create your models here.

class STOCK(models.Model):
    name = models.CharField(max_length=10)
    cost = models.FloatField()
    
    def __str__(self):
        return self.name
    

class InsideTransection(models.Model):
    name = models.CharField(max_length=10)
    stock = models.ManyToManyField(STOCK, related_name='Transection')
    price = models.IntegerField()
    # change = models.FloatField()
    
    def __str__(self):
        return self.name
    
class Valuation(models.Model):
    market_cap = models.IntegerField()
    stock = models.OneToOneField(STOCK, on_delete=models.CASCADE, related_name='valuation')
    pe_ratio = models.FloatField()
    
    def __str__(self):
        return self.market_cap
    