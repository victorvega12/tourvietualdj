from django.shortcuts import render
from rest_framework import viewsets
from .models import EstatuaSimplificada
from .serializers import EstatuaSimplificadaSerializer


class EstatuaSimplificadaViewSet(viewsets.ModelViewSet):
   queryset = EstatuaSimplificada.objects.all()
   serializer_class = EstatuaSimplificadaSerializer

