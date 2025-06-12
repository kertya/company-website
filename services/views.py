from django.shortcuts import render
from .models import Service, ServiceCategory

def service_list(request):
    categories = ServiceCategory.objects.all()
    return render(request, 'services/list.html', {'categories': categories})

def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    return render(request, 'services/detail.html', {'service': service})


def home_view(request):
    return render(request, 'home.html')
