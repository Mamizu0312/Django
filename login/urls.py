from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [

    path('', views.loginpage, name="login"),
    path('success', views.successpage, name="success"),
    
]
