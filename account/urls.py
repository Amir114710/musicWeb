from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('login' , LoginView.as_view() , name='login'),
    path('register' ,  Register.as_view() , name='register'),
    path('logout' , logout_user , name="logout"),
]