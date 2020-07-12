from django import forms
from .models import *
from django.forms import ModelForm


class OngletForm(ModelForm):
    nom = forms.CharField(max_length = 50,
        label="Nom",
        widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    class Meta:
        model = Onglet
        fields = ['nom']
        
class DossierForm(ModelForm):
    nom = forms.CharField(max_length = 700,
        label="Nom",
        widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    info = forms.CharField(max_length = 700,
        label="Description",
        widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    class Meta:
        model = Dossier
        fields = ['nom', 'info']

class LienForm(ModelForm):

    lien_url = forms.CharField(max_length = 700,
        label="URL",
        widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    info = forms.CharField(max_length = 700,
        label="Description",
        widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    class Meta:
        model = Lien
        fields = ['lien_url', 'info']