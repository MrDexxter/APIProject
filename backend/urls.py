from django.urls import path
from backend.views import CapitalizeView

urlpatterns = [
    path('encapsulate/', CapitalizeView.as_view(), name='encapsulate_string'),
]