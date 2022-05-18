from django.urls import path
from .views import index ,filter

urlpatterns = [
    path('',index,name='home'),
    path('user/<int:id>',filter,name='user'),
]