from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.signin, name='signin'),
    path('maps/', views.default_map, name='maps'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', RedirectView.as_view(url='accounts/login/', permanent=True)),
    path('login', RedirectView.as_view(url='accounts/login/', permanent=True)),
    path('signup/', views.signup),
    path('signup', views.signup)
]