from rest_framework import generics, filters
from .models import Medicament
from .serializers import MedicamentSerializer


class MedicamentListAPIView(generics.ListAPIView):
    queryset = Medicament.objects.all().order_by("nom")
    serializer_class = MedicamentSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ["nom", "cis"]


class MedicamentDetailAPIView(generics.RetrieveAPIView):
    """
    API lecture seule – détail d’un médicament par CIS
    """
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
    lookup_field = "cis"
