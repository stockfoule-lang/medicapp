from rest_framework import serializers
from .models import Medicament


class MedicamentSerializer(serializers.ModelSerializer):
    notice_bdpm_url = serializers.ReadOnlyField()

    class Meta:
        model = Medicament
        fields = [
            "cis",
            "nom",
            "forme_pharmaceutique",
            "laboratoire",
            "substance_active",
            "source_reglementaire",
            "date_mise_a_jour",
            "notice_bdpm_url",
        ]
