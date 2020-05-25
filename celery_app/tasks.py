# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
# from quick_publisher.celery import app
from .models import Auctions, Prices
import datetime


# from demoapp.models import Widget


@shared_task
def test_task():
    return print('cron it works! 2')

@shared_task
def update_post_status():
    date = datetime.datetime.now()
    dateyear = int(date.year)
    datemonth = date.month
    dateday = date.day - 1
    yesterday = datetime.date(dateyear, datemonth, dateday)
    
    today_auctions = Auctions.objects.filter(start_auction=date)

    yesterday_auctions = Auctions.objects.filter(start_auction=yesterday)

    print('yesterday date', yesterday)
    for ya in yesterday_auctions:
        print('yesterday_auctions before', ya.id, ' ', ya.status)
        ya.status = 3
        print('yesterday_auctions after', ya.status)
        ya.save()

    for i in today_auctions:
        if i.status != 2:
            print('today_auctions before', i.id, ' ', i.status)
            i.status = 2
            print('today_auctions after', i.status)
            i.save()

            p = Prices(new_price = i.start_price, auction=i, buyer_id=i.seller, winner=1)
            p.save()
    # p_del = Prices.objects.get(id=159)
    # p_del.delete()

    return print('status of yesterday auctions was update')




@shared_task
def add_first_price():
    pass



@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

