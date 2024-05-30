from django.urls import path
from . import views

urlpatterns = [
    path('data/',views.one_file, name="one_file"),
    
] 
