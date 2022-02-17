from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('signin/', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
]
