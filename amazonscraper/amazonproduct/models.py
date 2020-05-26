from django.db import models

# Create your models here.
class searchitem(models.Model):
    item_name= models.TextField()
    item_price= models.DecimalField(decimal_places=2,max_digits=5)
    item_rating = models.DecimalField(decimal_places=2,max_digits=5)
    item_numrating = models.PositiveIntegerField()