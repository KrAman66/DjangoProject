from django.contrib import admin
from django.urls import path, include
from first import views

#from : Package / folder
#import : Module / class / file
     
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='default'),
    path('about/', views.about,name='about'),
    
    path('demo/',include('demo.urls')),
    path('auth/',include('authenticate.urls')),
]

