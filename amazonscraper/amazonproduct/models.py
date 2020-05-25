from django.db import models

# Create your models here.
class searchitem(models.Model):
    item_name= models.TextField()
    item_price= models.DecimalField()
    item_rating = models.DecimalField()
    item_numrating = models.PositiveIntegerField()