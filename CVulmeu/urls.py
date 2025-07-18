from django.urls import path
from .views import *

urlpatterns = [path('', pagina_efectiva, name ="paginaefectiva_url"),
               path('mesaj-trimis', confirmare_mesaj, name='mesaj_trimis')]