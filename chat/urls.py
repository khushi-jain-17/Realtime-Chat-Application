from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register_user,name='register_user'),
    path('login',views.login_user,name='login_user'),
    path('logout',views.logout_user,name='logout_user'),
    path('',views.home,name='home'),
    path('<str:room>/',views.room,name='room'),
    path('checkview',views.checkview,name='checkview'),
    path('send',views.send,name='send'),
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),
]
