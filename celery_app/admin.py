from django.contrib import admin
from .models import Auctions, Bids, Prices

# Register your models here.
admin.site.register(Auctions)
admin.site.register(Bids)
admin.site.register(Prices)