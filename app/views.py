from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from app.models import Assodossierlien, Assoongletdossier, Assoongletlien, Dossier, Lien, Onglet
from app.forms import DossierForm, LienForm, OngletForm


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

def addonglet(request):
    form = OngletForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        created_by = request.user
        nom = form.cleaned_data.get("nom")
        onglet = Onglet.objects.create(
            nom = nom,
            created_by = created_by
        )
        onglet.save()
        return redirect("/onglet/"+str(onglet.id))
        
    return render(request,"add.html",locals())

def addongletdossier(request, idOnglet):
    form = DossierForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        onglet = get_object_or_404(Onglet, pk = idOnglet)
        nom = form.cleaned_data.get("nom")
        info = form.cleaned_data.get("info")
        dossier = Dossier.objects.create(
            nom = nom,
            info = info
        )
        dossier.save()
        assoongletdossier = Assoongletdossier.objects.create(
            onglet = onglet,
            dossier = dossier
        )
        assoongletdossier.save()
        
        return redirect("/onglet/"+str(onglet.id))
        
    return render(request,"add.html",locals())

def addongletlien(request, idOnglet):
    form = LienForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        onglet = get_object_or_404(Onglet, pk = idOnglet)
        lien_url = form.cleaned_data.get("lien_url")
        info = form.cleaned_data.get("info")
        lien = Lien.objects.create(
            lien_url = lien_url,
            info = info
        )
        lien.save()
        assoongletlien = Assoongletlien.objects.create(
            onglet = onglet,
            lien = lien
        )
        assoongletlien.save()
        
        return redirect("/onglet/"+str(idOnglet))
        
    return render(request,"add.html",locals())

def adddossierlien(request, idOnglet,idDossier):
    form = LienForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        dossier = get_object_or_404(Dossier, pk = idDossier)
        lien_url = form.cleaned_data.get("lien_url")
        info = form.cleaned_data.get("info")
        lien = Lien.objects.create(
            lien_url = lien_url,
            info = info
        )
        lien.save()
        assodossierlien = Assodossierlien.objects.create(
            dossier = dossier,
            lien = lien
        )
        assodossierlien.save()
        
        return redirect("/onglet/"+str(idOnglet)+"/dossier/"+str(idDossier))
        
    return render(request,"add.html",locals())


def adddossierdossier(request, idOnglet,idDossierPere):
    form = DossierForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        nom = form.cleaned_data.get("nom")
        info = form.cleaned_data.get("info")
        dossier = Dossier.objects.create(
            nom = nom,
            info = info,
            pere_id = idDossierPere
        )
        dossier.save()
        
        return redirect("/onglet/"+str(idOnglet)+"/dossier/"+str(idDossierPere))
        
    return render(request,"add.html",locals())

def updateonglet(request, idOnglet):
    onglet = get_object_or_404(Onglet, pk = idOnglet)
    dico = onglet.__dict__
    if request.method == "POST":
        nom = request.POST.get("nom")
        Onglet.objects.filter(pk = idOnglet).update(
            nom = nom
        )
        return redirect("/onglet/"+str(idOnglet))
    return render(request, "update.html", locals())


def updatedossier(request, idOnglet, idDossier):
    dossier = get_object_or_404(Dossier, pk = idDossier)
    dico = dossier.__dict__
    if request.method == "POST":
        nom = request.POST.get("nom")
        info = request.POST.get("info")
        Dossier.objects.filter(pk = idDossier).update(
            nom = nom,
            info = info
        )
        if(dossier.pere_id == -1):
            return redirect("/onglet/"+str(idOnglet))
        else:
            return redirect("/onglet/"+str(idOnglet)+"/dossier/"+str(dossier.pere_id))
        
    return render(request, "update.html", locals())

def updatedos(request, idOnglet, idDossier):
    dossier = get_object_or_404(Dossier, pk = idDossier)
    dico = dossier.__dict__
    if request.method == "POST":
        nom = request.POST.get("nom")
        info = request.POST.get("info")
        Dossier.objects.filter(pk = idDossier).update(
            nom = nom,
            info = info
        )
        
        return redirect("/onglet/"+str(idOnglet)+"/dossier/"+str(idDossier))
        
    return render(request, "update.html", locals())

def updateongletlien(request, idOnglet, idLien):
    lien = get_object_or_404(Lien, pk = idLien)
    dico = lien.__dict__
    if request.method == "POST":
        lien_url = request.POST.get("lien_url")
        info = request.POST.get("info")
        Lien.objects.filter(pk = idLien).update(
            lien_url = lien_url,
            info = info
        )
        return redirect("/onglet/"+str(idOnglet))
    return render(request, "update.html", locals())

def updatedossierlien(request, idOnglet, idDossier, idLien):
    lien = get_object_or_404(Lien, pk = idLien)
    dico = lien.__dict__
    if request.method == "POST":
        lien_url = request.POST.get("lien_url")
        info = request.POST.get("info")
        Lien.objects.filter(pk = idLien).update(
            lien_url = lien_url,
            info = info
        )
        return redirect("/onglet/"+str(idOnglet)+"/dossier/"+str(idDossier))
    return render(request, "update.html", locals())
