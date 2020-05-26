from django.conf.urls import url
from django.urls import re_path, path, include
from .views import Index, CreateAuction, RegisterUserView, Account_page
# from .views import LoginUserView, LogOutUserView
from django.conf.urls.static import static
from celery_proj.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    re_path(r'^$', Index.as_view(), name='index'),

    path('account-page', Account_page.as_view(), name='account_page'),
    
    url('create', CreateAuction.as_view(), name='create_auction'),
    url('register', RegisterUserView.as_view(), name='register_page'),

    path('accounts/', include('django.contrib.auth.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)