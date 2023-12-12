from rest_framework import serializers 
from .models import EstatuaSimplificada
class EstatuaSimplificadaSerializer(serializers.ModelSerializer):
  class Meta:
      model = EstatuaSimplificada
      fields = ['nombre', 'id', 'descripcion', 'modelo', 'ubicacion']