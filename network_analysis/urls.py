from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('analyze_pcap/', views.analyze_pcap, name='analyze_pcap'),
    path('wireshark/', views.wireshark_instructions, name='wireshark_instructions'),
]
