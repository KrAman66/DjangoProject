from django.urls import path
from add import views

urlpatterns=[
    path('calc/',views.home,name='home'),
    path('disp/',views.display_con,name='addition'),
    path('srch/',views.database_src,name='disp'),
    
   
]