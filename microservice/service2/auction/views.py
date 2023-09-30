from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import auction
from .serializers import auctionserializer
# Create your views here.
@api_view(['GET'])
def auctionObjects(request):
    cur = auction.objects.all()
    data = [{'auction_id' : i.auction_id,'start time' : i.start_time,'end_time' : i.end_time,'start price' : i.start_price,'item_name':i.item_name,'winner' : i.user} for i in cur]
    return Response({'data' : data})

@api_view(['POST'])
def addauction(request):
    serializer = auctionserializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'auction created'})
    return Response({'message': serializer.errors})


