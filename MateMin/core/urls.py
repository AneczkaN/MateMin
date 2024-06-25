# core/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('calculator/', views.calculator, name='calculator'),
    path('educational-links/', views.educational_links, name='educational_links'),
    path('task_list/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('add_task/', views.add_task, name='add_task'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
