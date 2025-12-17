from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, external_users ,dashboard


router = DefaultRouter()
router.register('leads', LeadViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('external-users/', external_users),
    path('dashboard/', dashboard),
]
