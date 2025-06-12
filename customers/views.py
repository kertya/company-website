from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Client

@login_required
def client_dashboard(request):
    client = Client.objects.get(user=request.user)
    return render(request, 'customers/dashboard.html', {'client': client})
