from django.urls import path
from django.conf.urls import url 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.signin, name='signin'),
    path('maps/', views.default_map, name='maps')
]