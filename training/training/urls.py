from django.contrib import admin
from django.urls import path, include
from training import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='default'),
    path('add/',include('add.urls')),

]
