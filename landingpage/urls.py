from django.urls import path
# import views
from . import views

urlpatterns = [
    # path/function/name
    path('', views.Home, name='Home'),
    
]
