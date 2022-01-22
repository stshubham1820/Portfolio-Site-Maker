from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard,name ='dashboard'),
    path('site',views.main,name='site'),
    path('servicedel',views.servicedel,name='servicedel'),
    path('intrestdel',views.intrestdel,name='intrestdel'),
    path('testdel',views.testdel,name='testdel'),
    path('imgdel',views.imgdel,name='imgdel'),
    path('serviceupdate',views.serviceupdate,name='serviceupdate'),
    path('intrestupdate',views.intrestupdate,name='intrestupdate'),
    path('testupdate',views.testupdate,name='testupdate'),
    path('imgupdate',views.imgupdate,name='imgupdate'),
    path('profileupdate',views.profileupdate,name='profileupdate'),
    path('aboutupdate',views.aboutupdate,name='aboutupdate'),
    path('resumeupdate',views.resumeupdate,name='resumeupdate'),
    path('userupdate',views.userupdate,name='userupdate'),
    path('changepass',views.changepass,name='changepass'),
    path('userinfo',views.userinfo,name='userinfo'),

]