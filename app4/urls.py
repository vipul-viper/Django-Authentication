
from django.contrib import admin
from django.urls import path,include
from .import views
app_name='app4'

urlpatterns = [
   path('',views.index,name='index'),
   path('register/',views.register,name='register'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout')

]
