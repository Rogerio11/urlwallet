from django.urls import path
from app.views import *

urlpatterns = [
    path("", home, name="home"),
    path("tes", test, name="test"),
    path("accueil", foncaccueil, name="accueil"),
    path("tes/<str:nom_onglet>",testonglet,name="testonglet"),
    path("onglet/<int:idOnglet>",fonconglet,name="onglet"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>",foncdossier, name="dossier"),
]