from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),  
    path('category', views.category, name='category'), 
    path('search', views.search, name='search'), 


]