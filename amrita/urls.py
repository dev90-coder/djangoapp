from django.contrib import admin
from django.urls import path
from amrita import views
urlpatterns = [
    path('',views.index,name='home'),
    path('index',views.index,name='home'),
    path('corner',views.corner,name='student'),
    path('registration',views.register,name='registration'),
    path('details',views.details,name='details'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    
    path('suggestions',views.suggest,name='suggestions'),
    path('about',views.abouts,name='about'),
    path('adminpanel',views.admins,name='admin')
]
