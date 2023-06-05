from django.urls import path
from authenticate import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.user_register,name='register'),
    path('login/',views.user_login,name='login'),
    path('success/',views.success,name='successr'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.user_profile,name='profile'),
    path('user_change/',views.user_change,name='user_change')
]
