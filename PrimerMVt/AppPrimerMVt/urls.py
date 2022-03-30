from django.urls import path

from AppPrimerMVt import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('familiares', views.familiares, name="Familiares"),
    
]
