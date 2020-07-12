from django.db import models

# Create your models here.

class Lien(models.Model):
    lien_url = models.CharField(max_length = 700)
    info = models.CharField(max_length = 700)
    
    class Meta:
        db_table = 'lien'
        
class Dossier(models.Model):
    nom = models.CharField(max_length = 700)
    info = models.CharField(max_length = 700)
    pere_id = models.IntegerField(default= -1)
    class Meta:
        db_table = 'dossier'
    
class Onglet(models.Model):
    nom = models.CharField(max_length = 50)
    class Meta:
        db_table = 'onglet'
        
class Assoongletdossier(models.Model):
    onglet = models.ForeignKey(Onglet, on_delete=models.CASCADE)
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    
class Assoongletlien(models.Model):
    onglet = models.ForeignKey(Onglet, on_delete=models.CASCADE)
    lien = models.ForeignKey(Lien, on_delete=models.CASCADE)
    
class Assodossierlien(models.Model):
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    lien = models.ForeignKey(Lien, on_delete=models.CASCADE)
    