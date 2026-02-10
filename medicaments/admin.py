from django.contrib import admin
from .models import Medicament

@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'substance_active', 'forme_pharmaceutique', 'laboratoire', 'date_mise_a_jour')
    search_fields = ('nom', 'substance_active', 'laboratoire')
    list_filter = ('forme_pharmaceutique', 'laboratoire')

