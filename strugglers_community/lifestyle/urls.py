from django.urls import path
from main import views

app_name = 'lifestyle'


urlpatterns= [
    path('', views.index, name='index'),
    
]