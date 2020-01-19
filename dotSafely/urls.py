
from django.contrib import admin
from django.urls import path, include
from safely import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name ='index'),
    path('card/', views.card, name ='card'),
    path('settings/', views.settings, name ='settings'),
    path('safeRoutes/', views.safeRoutes, name ='safeRoutes'),    
    path('SOS/', views.SOS, name ='SOS'),
    path('random/', views.random, name ='random'),
    path('markUnsafe/', views.markUnsafe, name ='markUnsafe'),
   
 path('safey/', views.safey, name ='safey'),
    path('timer/',views.timer,name='timer'),
]
