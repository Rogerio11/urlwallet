from django.contrib import admin
from app.models import Onglet, Dossier, Lien, Assoongletdossier, Assoongletlien, Assodossierlien

# Register your models here.
admin.site.register(Onglet)
admin.site.register(Dossier)
admin.site.register(Lien)
admin.site.register(Assoongletdossier)
admin.site.register(Assoongletlien)
admin.site.register(Assodossierlien)