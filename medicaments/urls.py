from django.urls import path
from .views import MedicamentListAPIView, MedicamentDetailAPIView

urlpatterns = [
    path("medicaments/", MedicamentListAPIView.as_view()),
    path("medicaments/<str:cis>/", MedicamentDetailAPIView.as_view()),
]
