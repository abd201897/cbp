from django.urls import path
from . import views

app_name = 'itreporting'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/',views.about, name= 'about')
]