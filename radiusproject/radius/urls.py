from django.urls import path, include
from django.conf.urls import url 
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('', views.signin, name='signin'),
    path('maps/', views.default_map, name='maps'),
    path('maps/', views.default_map, name='maps'),
    path('account/', include('django.contrib.auth.urls')),
]