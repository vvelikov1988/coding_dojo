from django.urls import path     
from . import views
urlpatterns = [
    path('', views.form),
    path('results', views.results),
]		   