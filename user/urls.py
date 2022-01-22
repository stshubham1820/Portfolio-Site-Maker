from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.info),
    path('logout',views.Logout,name='logout'),
]