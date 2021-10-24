from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html', {'title': 'Home'})


def signin(request):
    return render(request, 'sign-in-page.html', {'title': 'Sign in'})


# map
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'maps.html',
                  {'mapbox_access_token': mapbox_access_token})
