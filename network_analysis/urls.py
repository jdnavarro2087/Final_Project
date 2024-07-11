from django.urls import path
from . import views

urlpatterns = [
    path('analyze_pcap/', views.analyze_pcap, name='analyze_pcap'),
]
