from django.urls import path
from career import views

app_name = 'career'


urlpatterns= [
    path('', views.index, name='index'),
    
]