import os
import django
import requests
import xml.etree.ElementTree as ET

# 1️⃣ Configurer Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from medicaments.models import Medicament

# 2️⃣ Télécharger le fichier XML ANSM
url = "URL_DU_FICHIER_XML_ANSM"  # Remplace par l'URL officielle ANSM
response = requests.get(url)

if response.status_code == 200:
    with open("medicaments_ansm.xml", "wb") as f:
        f.write(response.content)
    print("Fichier ANSM téléchargé !")
else:
    print("Erreur de téléchargement :", response.status_code)
    exit()

# 3️⃣ Parser le fichier XML
tree = ET.parse("medicaments_ansm.xml")
root = tree.getroot()

# 4️⃣ Importer chaque médicament dans Django
count = 0
for med in root.findall('medicament'):
    nom = med.find('denomination').text
    substance = med.find('substance').text
    forme = med.find('forme').text
    labo = med.find('laboratoire').text
    notice_fr = med.find('notice_fr').text

    if not Medicament.objects.filter(nom=nom).exists():
        Medicament.objects.create(
            nom=nom,
            substance_active=substance,
            forme_pharmaceutique=forme,
            laboratoire=labo,
            notice_fr=notice_fr,
            notice_en="",  # Pas de traduction
            source_reglementaire="ANSM"
        )
        count += 1

print(f"{count} médicaments ont été ajoutés depuis le fichier ANSM !")
