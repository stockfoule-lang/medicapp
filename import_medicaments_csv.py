import os
import django
import csv

# 1️⃣ Configurer Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

# 2️⃣ Importer le modèle Medicament
from medicaments.models import Medicament

# 3️⃣ Chemin vers le fichier CSV
csv_file = 'medicaments.csv'  # Assure-toi que ce fichier est dans le même dossier

# 4️⃣ Lire le CSV et ajouter les médicaments
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        # Crée un nouveau médicament si il n'existe pas déjà
        if not Medicament.objects.filter(nom=row['nom']).exists():
            Medicament.objects.create(
                nom=row['nom'],
                substance_active=row['substance_active'],
                forme_pharmaceutique=row['forme_pharmaceutique'],
                laboratoire=row['laboratoire'],
                notice_fr=row['notice_fr'],
                notice_en=row['notice_en'],
                source_reglementaire=row.get('source_reglementaire', 'ANSM')
            )
            count += 1

print(f"{count} médicaments ont été ajoutés depuis le CSV !")
