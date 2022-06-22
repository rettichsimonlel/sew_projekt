from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Content
from django.template import loader

# Create your views here.

def index_view(request):
    contents = Content.objects.all()
    template = loader.get_template('html/model.html')
    pairs = []
    for i, item in enumerate(contents):
        b = i%2 == 0
        pairs.append({"item": item, "left": b})

    context = {
        'contents': pairs,
    }
    return HttpResponse(template.render(context, request))

def login_view(request):
    return render(request, 'html/login.html')

def register_view(request):
    return render(request, 'html/register.html')

def creating_view(request):
    return render(request, 'html/add.html')

def creating_send_view(request):
    if request.method == 'POST':
        m_title = request.POST.get('title', None)
        m_body = request.POST.get('body', None)
        m_user_name = str(request.user)

        new_content = Content.objects.create(title=m_title, body=m_body, user_name=m_user_name)
        new_content.save()

        #new_content = Content()
        #new_content.title = title
        #new_content.body = body
        #new_content.user_name = user_name
        #new_content.save()
        print(request.user)
    return redirect('/')

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

def logout_view(request):
    logout(request)
    return redirect('/')
