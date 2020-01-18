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
import geocoder


client = pymongo.MongoClient("mongodb+srv://"+str(os.getenv("USER"))+":"+str(os.getenv("PASSWORD"))+"@devcluster-qbbgy.mongodb.net/Sahyog?retryWrites=true&w=majority")
db = client.Sahyog
users = db.Location

def timer(request):
   return render(request, 'myView/timer.html')

def safey(request):
   return render(request, 'myView/safeRoute.html')


def SOS(request):    
    g = geocoder.ip('me')
    print(g.latlng)
    myphnos =['+918657181141','+918879272265']   
   
    
    for i in myphnos:
        to = i
        client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
        response = client.messages.create(
        body='helo it me :)'+'http://www.google.com/maps/place/21.186,72.7641', 
        to=to, from_=os.getenv('TWILIO_PHONE_NUMBER'))

    return render(request, 'myView/sos.html')




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
        return render(request, 'myView/card.html')
    else:
        return render(request, 'myView/markUnsafe.html')

def safeRoutes(request):
    return render(request,'myView/safeRoutes.html')

