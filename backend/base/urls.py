from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base-home'),
    path('about/', views.about, name='base-about'),
    path('contact/', views.contact, name='base-contact'),
    path('art/', views.art, name='base-art'),
    path('portfolio/', views.portfolio, name='base-portfolio'),
]