from django.shortcuts import get_object_or_404, render
from app.models import Assodossierlien, Assoongletdossier, Assoongletlien, Dossier, Onglet

from django import template

register = template.Library()

@register.filter
def to_and(value):
    return value.replace("&","and")

# Create your views here.
def home(request):    
    return render(request,"index.html")


def test(request):
    onglets = Onglet.objects.all()
    dico = {}
    dicoTest = {}
    i = 0
    for ong in onglets:
        dico[ong.nom] = i
        onglet_dossiers = Assoongletdossier.objects.filter(onglet = ong)
        onglet_liens = Assoongletlien.objects.filter(onglet = ong)
        tabDossier = []
        tabLien = []
        for ong_dos in onglet_dossiers:
            tabDossier.append(ong_dos.dossier)
        for ong_lien in onglet_liens:
            tabLien.append(ong_lien.lien)
        dicoTest[ong.nom] = {'num' : i, 'dossiers' : tabDossier, 'liens' : tabLien}
        i+=1
    return render(request, "test.html",locals())

def foncaccueil(request):
    onglets = Onglet.objects.all()
    dico = {}
    i = 0
    for ong in onglets:
        onglet_dossiers = Assoongletdossier.objects.filter(onglet = ong)
        onglet_liens = Assoongletlien.objects.filter(onglet = ong)
        tabDossiers = []
        tabLiens = []
        for ong_dos in onglet_dossiers:
            tabDossiers.append(ong_dos.dossier)
        for ong_lien in onglet_liens:
            tabLiens.append(ong_lien.lien)
        dico[ong] = {'num' : i, 'dossiers' : tabDossiers, 'liens' : tabLiens}
        i+=1
    return render(request, "accueil.html",locals())

def testonglet(request, nom_onglet):
    onglets = Onglet.objects.all()
    dico = {}
    i = 0
    nom_ong = nom_onglet.replace("-", "_")
    for ong in onglets:
        dico[ong.nom] = i
        i+=1
    chaine = " un deux trois"

    return render(request, "test_onglet.html",locals())

def fonconglet(request, idOnglet):
    onglets = Onglet.objects.all()
    tabDossiers = []
    tabLiens = []
    
    currentOnglet = get_object_or_404(Onglet, pk = idOnglet)
    onglet_dossiers = Assoongletdossier.objects.filter(onglet = currentOnglet)
    onglet_liens = Assoongletlien.objects.filter(onglet = currentOnglet)
    
    for ong_dos in onglet_dossiers:
        tabDossiers.append(ong_dos.dossier)
    for ong_lien in onglet_liens:
        tabLiens.append(ong_lien.lien)

    return render(request, "onglet.html",locals())

def foncdossier(request, idOnglet, idDossier):
    currentOnglet = get_object_or_404(Onglet, pk = idOnglet)
    currentDossier = get_object_or_404(Dossier, pk = idDossier)
    onglets = Onglet.objects.all()
    tabDossiers = Dossier.objects.filter(pere_id = idDossier)
    tabLiens = []
    
    dossier_liens = Assodossierlien.objects.filter(dossier = currentDossier)
    
    for dos_lie in dossier_liens:
        tabLiens.append(dos_lie.lien)
        
    return render(request, "dossier.html", locals())