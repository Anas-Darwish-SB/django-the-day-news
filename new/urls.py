from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list,name='new_list'),
    path('<str:slug>',views.news_detail, name='new_detail'),
    path('add_news/',views.add_news, name='add_news'),
    path('add_category/',views.add_category, name='add_category'),
]