from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('journey/', views.JourneyView.as_view(), name='journey'),
    path('film/', views.FilmView.as_view(), name='film'),
    path('politics/', views.PoliticsView.as_view(), name='politics'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
