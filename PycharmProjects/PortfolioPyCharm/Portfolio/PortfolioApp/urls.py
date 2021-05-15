from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]