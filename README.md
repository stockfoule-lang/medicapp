🩺 MedicApp



MedicApp est une application web permettant de rechercher des médicaments commercialisés en France et d’accéder directement à leurs fiches officielles issues de la Base de Données Publique des Médicaments (BDPM).



L’application ne réalise aucune interprétation médicale et se limite strictement à l’affichage d’informations réglementaires officielles.



🎯 Objectif du projet



Faciliter l’accès aux informations officielles et publiques sur les médicaments



Proposer une interface simple, rapide et compréhensible



Garantir une information fiable, traçable et sans transformation



🚫 Ce que MedicApp ne fait PAS



❌ Aucun conseil médical



❌ Aucune posologie interprétée



❌ Aucune recommandation thérapeutique



❌ Aucun diagnostic



👉 MedicApp ne remplace pas un professionnel de santé.



🗂️ Sources des données



Les données proviennent exclusivement de sources officielles françaises :



Base de Données Publique des Médicaments (BDPM)

https://base-donnees-publique.medicaments.gouv.fr



ANSM – Agence nationale de sécurité du médicament



Les fichiers BDPM utilisés :



CIS\_bdpm.txt



CIS\_InfoImportantes\_YYYYMMDD\_bdpm.txt



🏗️ Architecture technique

🔹 Backend



Python



Django



Django REST Framework



Base de données SQLite



Import automatique des données BDPM



➡️ Fournit une API REST locale utilisée par le frontend



🔹 Frontend



Flutter (Web)



Interface responsive



Lancement sur navigateur (Chrome)



➡️ Consomme l’API et affiche les résultats



🔄 Fonctionnalités principales



🔍 Recherche de médicaments par nom



📄 Affichage des informations réglementaires



🔗 Bouton « Voir la notice officielle sur BDPM »



🌐 Ouverture directe de la fiche officielle BDPM dans le navigateur



▶️ Lancer le projet en local

1️⃣ Backend (Django)

cd projet\_medicaments

python manage.py runserver





API disponible sur :



http://127.0.0.1:8000/api/medicaments/



2️⃣ Frontend (Flutter Web)

cd medicaments\_app

flutter run -d chrome



⚖️ Mentions légales



Les informations affichées dans MedicApp sont issues de données publiques mises à disposition par les autorités françaises.



📌 MedicApp est un outil d’information

📌 Il ne remplace pas un avis médical

📌 Toujours consulter un professionnel de santé



🚀 État du projet



✅ Backend fonctionnel

✅ API opérationnelle

✅ Import BDPM validé

✅ Frontend Flutter connecté

✅ Bouton BDPM fonctionnel



📌 Auteur



Projet développé à des fins pédagogiques et exploratoires, avec une attention particulière portée à la fiabilité des sources et au respect du cadre réglementaire.



💡 MedicApp — l’accès simple aux informations officielles sur les médicaments.

