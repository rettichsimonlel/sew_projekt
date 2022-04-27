from django.shortcuts import render
from .models import User
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'html/model.html')

def login(request):
    return render(request, 'html/login.html')

# https://stackoverflow.com/questions/25028895/very-simple-user-input-in-django
# TODO put other .html files instead of HttpResponse
def search(request):
    if request.method == 'POST':
        username_id = request.POST.get('username', None)
        password_id = request.POST.get('password', None)
        try:
            user = User.objects.get(username = username_id)
            #do something with user
            try:
                pwd = User.objects.get(password = password_id)
            except User.DoesNotExist:
                return HttpResponse(f"wrong password ({password_id})")
            html = ("<H1>%s</H1>", user)
            return HttpResponse(html)
        except User.DoesNotExist:
            return HttpResponse(f"no such user ({username_id})")  
    else:
        return render(request, 'model.html')
