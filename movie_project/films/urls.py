from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='films_home'),
    path('create_films',views.create_films,name='add_films'),
]