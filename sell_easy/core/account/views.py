from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django. core.exceptions import ValidationError
from .models import Profile

# Create your views here.

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)



    #return render(request, 'account/login.html', {'form': form})

    
def signup(request):
    return HttpResponse('User Signed in')

def dasboard(request):
    user_id = request.session['user_id']
    user = Profile.objects.get(id=user)
    return render(request, 'account/dasboard.html', {'user':user})



