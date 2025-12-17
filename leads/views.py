from rest_framework.viewsets import ModelViewSet
from .models import Lead
from .serializers import LeadSerializer
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.db.models import Count

class LeadViewSet(ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

@api_view(['GET'])
def external_users(request):
    url = "https://randomuser.me/api/?results=5"
    response = requests.get(url)
    return Response(response.json())
def dashboard(request):
    data = (
        Lead.objects
        .values('source')
        .annotate(count=Count('id'))
    )
    return render(request, 'dashboard.html', {'data': data})
