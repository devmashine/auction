from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Auctions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    status = models.IntegerField(blank = True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank = True)
    start_price = models.IntegerField()
    bid_up = models.IntegerField()
    start_auction = models.DateField()
    sort_auction = models.IntegerField(blank = True)
    main_img = models.ImageField(upload_to='file', blank=True)
#
# class ImgForAuction(models.Model):
#     auction = models.ForeignKey(Auctions, on_delete=models.CASCADE, blank=True)
#     our_img = models.ImageField(upload_to='file', blank=True)


class Bids(models.Model):
    auction = models.ForeignKey(Auctions, on_delete=models.CASCADE)
    bid = models.IntegerField(blank = True)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now=True)

class Prices(models.Model):
    new_price = models.IntegerField()
    auction = models.ForeignKey(Auctions, on_delete=models.CASCADE)
    new_price_time = models.DateTimeField(auto_now=True)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    winner = models.IntegerField(blank = True)