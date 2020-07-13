from django.urls import path
from app.views import *

urlpatterns = [
    path("", home, name="home"),
    path("accueil", foncaccueil, name="accueil"),
    path("onglet/<int:idOnglet>",fonconglet,name="onglet"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>",foncdossier, name="dossier"),
    path("onglet/ajout",addonglet,name="ongletajout"),
    path("onglet/<int:idOnglet>/dossier/ajout",addongletdossier,name="ongletajoutdossier"),
    path("onglet/<int:idOnglet>/lien/ajout",addongletlien,name="ongletajoutlien"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>/lien/ajout",adddossierlien,name="dossierajoutlien"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossierPere>/dossier/ajout",adddossierdossier,name="dossierajoutdossier"),
    path("onglet/<int:idOnglet>/update-delete", update_delete_onglet, name = "updatedeleteonglet"),
    path("onglet/<int:idOnglet>/update", updateonglet, name = "update"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>/update-delete", update_delete_dossier, name = "updatedeletedossier"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>/update", updatedossier, name = "updatedossier"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>/upd-del", update_delete_dossier_dossier, name = "updatedeldos"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>/upd", updatedos, name = "updatedos"),
    path("onglet/<int:idOnglet>/lien/<int:idLien>/update-delete",update_delete_update_onglet_lien, name = "updatedeleteongletlien"),
    path("onglet/<int:idOnglet>/lien/<int:idLien>/update", updateongletlien, name = "updateongletlien"),  
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>/lien/<int:idLien>/update-delete",update_delete_update_dossier_lien, name = "updatedeletedossierlien"),
    path("onglet/<int:idOnglet>/dossier/<int:idDossier>/lien/<int:idLien>/update", updatedossierlien, name = "updatedossierlien"),   
]