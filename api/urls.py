from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('tenants/', views.getTenants),
    path('tenants/create', views.createTenant),
    path('tenants/<str:pk>/update', views.updateTenant),
    path('tenants/<str:pk>', views.getTenant),
    path('tenants/<str:pk>/delete', views.deleteTenant),
]