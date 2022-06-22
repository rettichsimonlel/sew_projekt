from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('login.html/', views.login_view, name='login_view'),
    path('login.html/send/', views.search_view, name='search_view'),
    path('login.html/register.html/', views.register_view, name='search_view'),
    path('login.html/register.html/send/', views.data_input_view, name='search_view'),
    path('add.html/', views.creating_view, name='creating_view'),
    path('add.html/send/', views.creating_send_view, name='creating_send_view'),
    path('logout/', views.logout_view, name='logout_view')
]
