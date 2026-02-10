from pathlib import Path
from medicaments.models import Medicament


BASE_DIR = Path(__file__).resolve().parent.parent.parent
FICHIER_NOTICES = BASE_DIR / "data" / "CIS_CPD_bdpm.txt"


def import_notices():
    if not FICHIER_NOTICES.exists():
        raise FileNotFoundError(
            f"Fichier introuvable : {FICHIER_NOTICES}"
        )

    compteur = 0

    with open(FICHIER_NOTICES, encoding="latin-1") as f:
        for ligne in f:
            champs = ligne.strip().split("\t")

            # Format officiel BDPM
            cis_medicament = champs[0]
            cis_notice = champs[1]
            type_doc = champs[2]

            # On ne garde QUE les notices
            if type_doc != "NOTICE":
                continue

            try:
                medicament = Medicament.objects.get(cis=cis_medicament)

                medicament.notice_url_fr = (
                    f"https://base-donnees-publique.medicaments.gouv.fr/"
                    f"medicament/{cis_notice}/extrait"
                )

                medicament.save(update_fields=["notice_url_fr"])
                compteur += 1

            except Medicament.DoesNotExist:
                continue

    print(f"✅ {compteur} notices BDPM importées avec succès")
