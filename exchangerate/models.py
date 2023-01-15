from django.db import models
from django.utils import timezone

# Create your models here.
class Exchangerate(models.Model): 
    end_of_day = models.CharField(max_length=10)
    usd = models.DecimalField(max_digits = 8, decimal_places = 6)
    cny = models.DecimalField(max_digits = 8, decimal_places = 6)
    jpy = models.DecimalField(max_digits = 8, decimal_places = 6)
    cad = models.DecimalField(max_digits = 8, decimal_places = 6)
    aud = models.DecimalField(max_digits = 8, decimal_places = 6)
    sgd = models.DecimalField(max_digits = 8, decimal_places = 6)
    thb = models.DecimalField(max_digits = 8, decimal_places = 6)
    myr = models.DecimalField(max_digits = 8, decimal_places = 6)
    eur = models.DecimalField(max_digits = 8, decimal_places = 6)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    # def __str__(self) -> str:
    #     return f"{self.country} => {self.year} => {self.human_count}"