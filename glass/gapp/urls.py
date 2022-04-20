from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('web', views.web),
    path('git', views.git),
    path('home', views.home),
    
]
