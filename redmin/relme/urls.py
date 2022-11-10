from django.contrib import admin
from django.urls import path,include
from relme import views

urlpatterns = [
     path('',views.index,name='index')

]
