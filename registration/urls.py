from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
   #giriş sayfaları
   path("login/",views.login_request,name="login"),
   path("register",views.register_request,name="register"),
   path("logout",views.logout_request,name="logout"),

   
]
