from django.urls import path
from demo import views

urlpatterns=[
    path('',views.home,name='home'),
    path('display/',views.display,name='show'),
    path('display/edit/<int:id>',views.update,name='update'),
    path('display/delete/<int:id>',views.delete,name='delete'),
]