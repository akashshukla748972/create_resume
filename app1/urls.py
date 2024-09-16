from django.urls import path
from app1 import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name='login'),
    path('temp', views.temp, name='temp'),
]