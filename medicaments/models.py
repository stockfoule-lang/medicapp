from django.db import models


class Medicament(models.Model):
    cis = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="Code CIS"
    )

    nom = models.CharField(
        max_length=255,
        verbose_name="Nom du médicament"
    )

    forme_pharmaceutique = models.CharField(
        max_length=255,
        blank=True
    )

    laboratoire = models.CharField(
        max_length=255,
        blank=True
    )

    substance_active = models.TextField(
        blank=True
    )

    source_reglementaire = models.CharField(
        max_length=50,
        default="BDPM"
    )

    date_mise_a_jour = models.DateField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.nom} ({self.cis})"

    @property
    def notice_bdpm_url(self):
        """
        Lien officiel BDPM (FIABLE)
        """
        return (
            "https://base-donnees-publique.medicaments.gouv.fr/"
            f"medicament/{self.cis}"
        )
