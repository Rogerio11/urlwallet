from django.urls import path
from app.views import *

urlpatterns = [
    path("", home, name="home"),
    path("tes", test, name="test"),
    path("accueil", foncaccueil, name="accueil"),
    path("tes/<str:nom_onglet>",testonglet,name="testonglet"),
    path("onglet/<int:idOnglet>",fonconglet,name="onglet"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>",foncdossier, name="dossier"),
    path("onglet/ajout",addonglet,name="ongletajout"),
    path("onglet/<int:idOnglet>/dossier/ajout",addongletdossier,name="ongletajoutdossier"),
    path("onglet/<int:idOnglet>/lien/ajout",addongletlien,name="ongletajoutlien"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>/lien/ajout",adddossierlien,name="dossierajoutlien"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossierPere>/dossier/ajout",adddossierdossier,name="dossierajoutdossier"),
    path("onglet/<int:idOnglet>/update", updateonglet, name = "update"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>/update", updatedossier, name = "updatedossier"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>/upd", updatedos, name = "updatedos"),
    path("onglet/<int:idOnglet>/lien/<int:idLien>/update", updateongletlien, name = "updateongletlien"),  
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>/lien/<int:idLien>/update", updatedossierlien, name = "updatedossierlien"),   
]