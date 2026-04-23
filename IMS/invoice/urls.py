from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard-view'),
    path('invoice/', views.invoice, name = 'invoice-view'),
    path('profile/', views.profile, name = 'profile-view'),
    path('clients/', views.clients, name = 'clients-view'),
]
