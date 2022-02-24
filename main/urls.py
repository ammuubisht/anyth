from django.conf import settings
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static



urlpatterns = [
    path('', views.Home, name='Home'),
    path('about-anyth', views.AboutAnyth, name='about-anyth'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('create-account', views.CreateAccount, name='create-account'),
    path('ind-message/<int:pk>/', views.SingleMessage, name='ind-message'),
    path('my-circle', views.MyCircle, name='my-circle'),


    
    
] 