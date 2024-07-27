from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('forums/', views.forum_list, name='forum_list'),
    path('forum/create/', views.create_forum, name='create_forum'),
    path('forum/<int:forum_id>/', views.thread_list, name='thread_list'),
    path('thread/<int:thread_id>/', views.post_list, name='post_list'),
    path('forum/<int:forum_id>/create_thread/', views.create_thread, name='create_thread'),
    path('thread/<int:thread_id>/create_post/', views.create_post, name='create_post'),
    path('profile/', views.profile, name='profile'),
]
