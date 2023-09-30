from django.db import models

# Create your models here.
class auction(models.Model):
    auction_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_price  = models.IntegerField()
    item_name = models.CharField(max_length=80)
    user = models.CharField(max_length = 80,null = True)

