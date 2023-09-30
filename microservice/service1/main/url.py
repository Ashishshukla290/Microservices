from django.urls import path,include
from .views import RegisterUser,sample,AuctionAdmin
urlpatterns = [
    path('register/',RegisterUser.as_view()),
    path('sample/',sample.as_view()),
    path('addauction/',AuctionAdmin.as_view())
]