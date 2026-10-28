from django.urls import path

from . import views
from django.conf.urls.static import static

urlpatterns = [
      
    path("", views.index, name="index"),

    path('index/', views.index, name='index'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('login/', views.login, name='login'),

    path('signin/', views.signin, name='signin'),
]