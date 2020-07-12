from django import forms
from .models import *
from django.forms import ModelForm


class OngletForm(ModelForm):
    class Meta:
        model = Onglet
        fields = ['nom']
        
class DossierForm(ModelForm):
    class Meta:
        model = Dossier
        fields = ['nom', 'info']

class LienForm(ModelForm):
    class Meta:
        model = Lien
        fields = ['lien_url', 'info']