from django.shortcuts import render

# Create your views here.
def index(request):
    if(request.user.is_authenticated):
        return render(request, 'myView/card.html')
    return render(request, 'myView/index.html')

def home(request):
   return render(request, 'myView/card.html')

def settings(request):
   return render(request, 'myView/settings.html')