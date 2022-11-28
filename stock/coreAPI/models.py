from django.db import models

# Create your models here.

class STOCK(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    change = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class InsideTransaction(models.Model):
    name = models.CharField(max_length=10)
    stock = models.ForeignKey(STOCK, on_delete=models.CASCADE, related_name='Transaction')
    cost = models.FloatField()
    # change = models.FloatField()
    
    def __str__(self):
        return self.name
    
class Valuation(models.Model):
    market_cap = models.IntegerField()
    stock = models.OneToOneField(STOCK, on_delete=models.CASCADE, related_name='valuation')
    pe_ratio = models.FloatField()
    
    def __str__(self):
        return self.stock.name
    