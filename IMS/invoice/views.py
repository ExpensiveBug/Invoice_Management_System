from django.shortcuts import render

# Create your views here.

def invoice(request):
    return render(request, 'invoices.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')

def clients(request):
    return render(request, 'clients.html')