from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.auctionObjects),
    path('add/',views.addauction)
]