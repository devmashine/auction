from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import RegisterUserForm, AuctionsForm, BidUpForm

from django.views.generic import CreateView

from django.urls import reverse_lazy


from django.contrib.auth.models import User, Group
from .models import Auctions, Bids, Prices, ImgForAuction

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse
from django.forms.models import model_to_dict

from django.views.decorators.csrf import csrf_exempt

from django.core.files.base import ContentFile
from io import BytesIO
# Create your views here.

import ast

import datetime

class CreateAuction(LoginRequiredMixin, CreateView):
    model = Auctions
    template_name = 'create_auction.html'
    form_class = AuctionsForm
    success_url = reverse_lazy('index')
    success_msg = 'Auction was created'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CreateAuction, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the posts
        context['groups_user_sellers'] = User.objects.filter(groups=1)
        return context

    def form_valid(self, form):
        form_valid = super().form_valid(form)

        # Get and Save additional images
        id = form.save().pk
        auction = Auctions.objects.get(pk=id)
        files = self.request.FILES.getlist('files')
        if files:
            for file in files:
                fl = ImgForAuction(auction=auction, img = file)
                print('fl', fl)
                fl.save()


        
        return form_valid


class Index(View):

    def post(self, request):
        bidup_form = BidUpForm(request.POST)
        print('bidup_form view')
        if bidup_form.is_valid():
            print('bidup_form.cleaned_data[bid]')

            bid_data = bidup_form.save(commit=True)

            print('bid_data', bid_data)

            new_bid = bidup_form.cleaned_data['bid']
            auction = bidup_form.cleaned_data['auction']
            buyer = bidup_form.cleaned_data['buyer_id']

            print('auction', auction.id)
            prices = Prices.objects.filter(auction_id = auction.id)
            print('prices', prices)
            winner= 1

            price_for_main = new_bid
            for exist_price in prices:

                if new_bid < exist_price.new_price:
                    print('exist_price.new_price', exist_price.new_price, '> new_bid', new_bid)
                    winner=0
                    price_for_main = 'none'


            if winner == 1:
                winner_price = Prices.objects.filter(winner = 1, auction_id = auction.id)
                for win_old in winner_price:
                    win_old.winner=0
                    win_old.save()
                
                    
            new_price = Prices(new_price = new_bid, auction=auction, buyer_id=buyer, winner=winner)
            new_price.save()

            dict_bid_data = model_to_dict(bid_data)

            if price_for_main != 'none':
                dict_bid_data.update({"new_bid": price_for_main})
            print('model_to_dict(bid_data)', dict_bid_data)

        # return redirect('index')
        return JsonResponse({'bid_data': dict_bid_data}, status=200)


    def get(self, request):

        winners = Prices.objects.filter(winner=1)
        additional_img = ImgForAuction.objects.all() 
        groups_user_buyers = User.objects.filter(groups = 2)
        form = BidUpForm
        groups_user_sellers = User.objects.filter(groups = 1)

        auctions_tomorrow = Auctions.objects.filter(status=1).order_by('-start_auction')
        auctions_today = Auctions.objects.filter(status=2).order_by('-start_auction')
        auctions_yesterday = Auctions.objects.filter(status=3).order_by('-start_auction')

        prices = Prices.objects.filter()

        current_user = request.user
        auction_bids = Bids.objects.all()

        ctx ={
            'form': form,
            'winners': winners,
            'current_user': current_user,
            'additional_img': additional_img,
            'prices': prices,
            'auctions_today': auctions_today,
            'auctions_tomorrow': auctions_tomorrow,
            'auctions_yesterday': auctions_yesterday,
            'auction_bids': auction_bids,
            'groups_user_buyers': groups_user_buyers,
            'groups_user_sellers': groups_user_sellers,
        }
        return render(request, 'index.html', ctx)



# old registration
#
# class LoginUserView(LoginView):
#     template_name = 'login.html'
#     form_class = AuthUserForm
#     success_url = reverse_lazy('index')
#     success_msg = 'Hi, User'
#     def get_success_url(self):
#         return self.success_url
#
# class LogOutUserView(LogoutView):
#     next_page = reverse_lazy('index')

class RegisterUserView(CreateView):
    model = User
    template_name = 'register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')
    success_msg = 'User was created'


    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        group = form.cleaned_data["groups"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)

        group_id = group[0].id
        my_group = Group.objects.get(id = group_id)
        print('User.id', self.request.user.id)
        my_group.user_set.add(self.request.user.id)
        return form_valid
