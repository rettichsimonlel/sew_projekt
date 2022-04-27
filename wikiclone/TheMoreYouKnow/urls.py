from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html/', views.login, name='login'),
    path('login.html/send/', views.search, name='search'),
]
