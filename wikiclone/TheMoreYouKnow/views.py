from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    return render(request, 'html/model.html')

def login(request):
    return render(request, 'html/login.html')

def register(request):
    return render(request, 'html/register.html')

# https://stackoverflow.com/questions/25028895/very-simple-user-input-in-django
# TODO put other .html files instead of HttpResponse
def search(request):
    if request.method == 'POST':
        print("in request.method == 'POST'")
        username_id = request.POST.get('username', None)
        password_id = request.POST.get('password', None)
        user = authenticate(request, username=username_id, password=password_id)
        if user is not None:
            print(f"You are logged in mr. {username_id}")
            return  redirect('/') # for lack of a better idea
            # return HttpResponse(f"You are logged in mr. {username_id}")
        else:
            return HttpResponse("User not found")

#        try:
#            user = User.objects.get(username = username_id) # here the problem
#            print(user)
#            try:
#                pwd = User.objects.get(password = password_id)
#            except User.DoesNotExist:
#                return HttpResponse(f"wrong password ({password_id})")
#            html = ("<H1>%s</H1>", user)
#            return HttpResponse(html)
#        except User.DoesNotExist:
#            return HttpResponse(f"no such user ({username_id})")  
#    else:
#        return render(request, 'model.html')

# adding a new user to the database
def data_input(request):
    # TODO register
    return redirect('/')
    #return HttpResponse("it should be doing shit")
