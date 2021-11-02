from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from .forms import *
from django.views import generic
from .models import Activity


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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #process signup
            return HttpResponseRedirect('avatar.html')
    else:
        context = {
            'form': SignUpForm,
        }
        return render(request, 'registration/signup.html', context)


# map
@login_required
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'maps.html',
                  {'mapbox_access_token': mapbox_access_token})


# create activity
def create_activity(request):
    return render(request, 'create-activity-page.html')


# activity page
def activity(request):
    return render(request, 'activity-page.html')


# about page
def about(request):
    return render(request, 'about.html')


class ActivityListView(generic.ListView):
    model = Activity


class ActivityDetailView(generic.DetailView):
    model = Activity

