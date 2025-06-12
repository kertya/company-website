from django.contrib import admin
from django.urls import path
from services import views as service_views
from customers import views as customer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', service_views.service_list, name='service_list'),
    path('services/<int:pk>/', service_views.service_detail, name='service_detail'),
    path('dashboard/', customer_views.client_dashboard, name='dashboard'),
    path('', views.home_view, name='home'),
]