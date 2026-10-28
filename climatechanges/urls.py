from django.urls import path # type: ignore

from . import views
from django.conf.urls.static import static # type: ignore

urlpatterns = [
      
    path("", views.index, name="index"),

    path('index/', views.index, name='index'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('login/', views.login, name='login'),

   path('signup/', views.signup, name='signup'),
]
