from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('books/', views.books, name='books'),

    path('books/add/', views.add_book, name='add_book'),

    path('members/', views.members, name='members'),
      path('issues/', views.issues, name='issues'),


]