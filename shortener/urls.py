from django.contrib import admin
from django.urls import path


from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.create_link, name='create_link'),
    path('<str:hash_>/', views.redirect_link, name='redirect_link'),
]
