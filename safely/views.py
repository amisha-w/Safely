from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from django.http import HttpResponse
import datetime
from bson.json_util import dumps
import pymongo
import dns
import os
from dotenv import load_dotenv
from twilio.rest import Client
from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from django.http import HttpResponse
import datetime
from bson.json_util import dumps
import pymongo
import dns
import os
from dotenv import load_dotenv
from twilio.rest import Client

client = pymongo.MongoClient("mongodb+srv://"+str(os.getenv("USER"))+":"+str(os.getenv("PASSWORD"))+"@devcluster-qbbgy.mongodb.net/Sahyog?retryWrites=true&w=majority")
db = client.Sahyog
users = db.Location




# Create your views here.
def safey(request):
   return render(request, 'myView/safeRoute.html')


def SOS(request):
    myphnos =['+918657181141','+918879272265']   
    for i in myphnos:
        to = i
        client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
        response = client.messages.create(
        body='helo it me :)', 
        to=to, from_=os.getenv('TWILIO_PHONE_NUMBER'))
    return HttpResponse("hello")




def random(request):
    locations = dumps(users.find())
    #print(locations)
    return HttpResponse(
        "data: "+locations+"\n\n",
        content_type='text/event-stream'
    )

# Create your views here.
def index(request):
    if(request.user.is_authenticated):
        return render(request, 'myView/card.html')
    return render(request, 'myView/index.html')

def home(request):
   return render(request, 'myView/card.html')

def settings(request):
   return render(request, 'myView/settings.html')

def markUnsafe(request):
    if request.method == "POST":
        location = request.POST.get('location')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        #print("lat :",lat,"lng :",lng)
        #print('location: ',location)
        load_dotenv()        
        location = {"lat": lat, "lng": lng, "location": location }
        users.insert_one(location)        
        return HttpResponse(json.dumps({'status':'success','latitude':lat,'longitude':lng}),content_type='application/json')
    else:
        return render(request, 'myView/markUnsafe.html')

def safeRoutes(request):
    return render(request,'myView/safeRoutes.html')

