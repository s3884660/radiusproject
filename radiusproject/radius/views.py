from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#test activities
activities = [
    {
        'title': 'Activity 1',
        'description': 'First post content',
        'img' : 'logo_icon.png',
        'date_posted': 'October 4, 2021'
    },
        {
        'title': 'Activity 2',
        'description': 'Second post content',
        'img' : 'logo_icon.png',
        'date_posted': 'October 4, 2021'
    },
        {
        'title': 'Activity 3',
        'description': 'Third post content',
        'img' : 'logo_icon.png',
        'date_posted': 'October 4, 2021'
    }
]


#views

def index(request):
    context = {
        'activities': activities
    }
    return render(request, 'index.html', context)


def signin(request):
    return render(request, 'sign-in-page.html', {'title': 'Sign in'})


# login
def login(request):
    return render(request, 'login.html')


# signup
def signup(request):
    return render(request, 'signup.html')


# map
@login_required
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'maps.html',
                  {'mapbox_access_token': mapbox_access_token})
