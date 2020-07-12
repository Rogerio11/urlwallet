from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lien(models.Model):
    lien_url = models.CharField(max_length = 700)
    info = models.CharField(max_length = 700)
    created_at = models.DateTimeField(auto_now_add=True)   
    class Meta:
        db_table = 'lien'
        
class Dossier(models.Model):
    nom = models.CharField(max_length = 700)
    info = models.CharField(max_length = 700)
    pere_id = models.IntegerField(default= -1)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'dossier'
    
class Onglet(models.Model):
    nom = models.CharField(max_length = 50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
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
    