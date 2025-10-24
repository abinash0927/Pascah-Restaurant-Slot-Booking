from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import DiningTable,Customer
from .serializers import TableSerializer,CustomerSerializer
from queue import Queue

from vonage import Vonage,Auth,HttpClientOptions
from vonage_sms import SmsMessage
from vonage_http_client import HttpClient


# Create your views here.
que = []
client = Vonage(Auth(api_key="41a90dd3",api_secret="1tqNfEYy8hAN8hqJ"))
def Homepage(request):
    dining = DiningTable
    customer = Customer
    for i in range(len(dining.objects.filter(status=False))):
        if len(que) > 0 :
            cus = que.pop(0)
            customer.objects.create(name=cus[0],contact=cus[1],table=dining.objects.filter(status=False).first())
            dining.objects.filter(table_no=dining.objects.filter(status=False).first().table_no).update(status=True)
            msg = SmsMessage(to=f'91{cus[1]}',from_='Pascah',text=f"Your assigned dining table no.{dining.objects.filter(status=False).first().table_no - 1}")
            resonseData = client.sms.send(msg)
            print(resonseData)
        else:
            break
    # print(len(dining.objects.filter(status=False)))
    # print(dining.objects.filter(status=False).first().table_no)
    on_hold = dining.objects.filter(status=True)
    cont = {
    'queues': que,
    'on_holds':on_hold,
    }
    return render(request,'Home.html',context=cont)


def Bookpage(request):
    if request.method == 'POST':
        que.append([request.POST.get('name'),request.POST.get('contact')])
        return redirect('/')
    return render(request,'book.html')

class ListView(ListCreateAPIView):
    queryset = DiningTable.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListTableView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
     
class ListupdateView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'table'
     