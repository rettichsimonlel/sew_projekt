from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

def index_view(request):
    return render(request, 'html/model.html')

def login_view(request):
    return render(request, 'html/login.html')

def register_view(request):
    return render(request, 'html/register.html')

# https://stackoverflow.com/questions/25028895/very-simple-user-input-in-django
# TODO put other .html files instead of HttpResponse
def search_view(request):
    if request.method == 'POST':
        print("in search == 'POST'")
        username_id = request.POST.get('username', None)
        password_id = request.POST.get('password', None)
        print(username_id)
        user = authenticate(request, username=username_id, password=password_id)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login.html')


# adding a new user to the database
def data_input_view(request):
    # TODO register
    if request.method == 'POST':
        new_username = request.POST.get('username', None)
        new_password = request.POST.get('password', None)
        new_user = User(username=new_username)
        new_user.set_password(new_password)
        new_user.save()
    else:
        print("Fail")
    return redirect('/')
    #return HttpResponse("it should be doing shit")
