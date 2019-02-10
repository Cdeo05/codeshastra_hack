from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('login/',LoginView.as_view('templates/login.html'),name='login')
    path('register/views.register,name='register)
]