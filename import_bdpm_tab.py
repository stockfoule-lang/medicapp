import os
import django
import csv

# Initialisation Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from medicaments.models import Medicament

FICHIER_BDPM =  r"C:\Users\user\Documents\projet_medicaments\bdpm\CIS_bdpm.txt"
  # ⚠️ adapte le nom si besoin

count = 0

with open(FICHIER_BDPM, encoding="latin-1", errors="ignore") as f:


    reader = csv.reader(f, delimiter="\t")  # 🔴 TABULATION
    for row in reader:
        if len(row) < 6:
            continue

        cis = row[0].strip()
        nom = row[1].strip()
        forme = row[2].strip()
        voie = row[3].strip()
        statut = row[4].strip()
        procedure = row[5].strip()

        if not Medicament.objects.filter(cis=cis).exists():
            Medicament.objects.create(
                cis=cis,
                nom=nom,
                forme_pharmaceutique=forme,
                laboratoire="",
                substance_active="",
                source_reglementaire="BDPM"
            )
            count += 1

print(f"{count} médicaments importés avec succès")
