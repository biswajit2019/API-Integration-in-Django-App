# from django.conf.urls import url
from django.urls import path
from crypto.views import home, prices

urlpatterns = [
    path('', home, name='home'),
    path('prices/', prices, name='prices'),
]