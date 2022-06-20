from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.index, name='index'),
    path('register/',views.register,name ='register'),
    path('login/',auth_views.LoginView.as_view(template_name='register/login.html'),name ='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='register/logout.html'),name ='logout'),
    path('profile/', views.profile, name='profile'),
    path('addhood/',views.create_neighborhood, name='addhood'),
    path('singlehood/<hood_id>/',views.display_hood, name='single-hood'),
    path('delete/<pk>',DeleteHood.as_view(),name='delete'),
    path('update/<pk>',UpdateHood.as_view(),name='update'),
    path('userprofile/<int:id>', views.user_profile, name='userprofile'),
    path('search/', views.search_business, name='search'),
    path('post/', views.create_post, name='post'),
    path('display_post/', views.display_post, name='display_post'),
    path('businessd/', views.business_details,name='businessd'),
    path('business/', views.business, name='business'),
   
]