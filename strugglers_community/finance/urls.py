from django.urls import path
from finance import views

app_name = 'finance'

urlpatterns= [
    path('', views.index, name='index'),
    
]