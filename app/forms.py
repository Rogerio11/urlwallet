from django import forms
from app.models import Onglet



class OngletForm(ModelForm):
    class Meta:
        model = Onglet
        fields = ['nom']
        