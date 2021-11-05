from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.abc, name='home'),
    path("about",views.about, name='About'),
     path("contact",views.contact, name='contact'),
      path("services",views.services, name='services'),
      path("feedback",views.feedback, name='feedback'),
    
     
      
]