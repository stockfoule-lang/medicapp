import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from medicaments.models import Medicament

BASE_URL = "https://base-donnees-publique.medicaments.gouv.fr/medicament/"

updated = 0

for med in Medicament.objects.all():
    med.notice_url_fr = f"{BASE_URL}{med.cis}"
    med.save(update_fields=["notice_url_fr"])
    updated += 1

print(f"{updated} notices liées avec succès")
