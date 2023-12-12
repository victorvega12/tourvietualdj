from django.db import models

#class Accesibilidad(models.Model):
#    nombre = models.CharField(max_length=255, null=True)
#   descripcion = models.TextField(null=True)
#    info_accesible = models.TextField(null=True)

#class CatalogoEstatuas(models.Model):
#    ruta_id = models.IntegerField(null=True)
#    accesibilidad = models.ForeignKey('Accesibilidad', on_delete=models.SET_NULL, null=True)

#class DispositivoMovil(models.Model):
#    modelo = models.CharField(max_length=100, null=True)
#    sistema_operativo = models.CharField(max_length=50, null=True)

#class Estatuas(models.Model):
#    nombre = models.CharField(max_length=255, null=True)
#    descripcion_detallada = models.TextField(null=True)
#    modelo_3d = models.TextField(null=True)
#    otra_informacion = models.TextField(null=True)
#    accesibilidad = models.ForeignKey('Accesibilidad', on_delete=models.SET_NULL, null=True)

#class InteraccionUsuarioEstatua(models.Model):
#    user_id = models.IntegerField(null=True)
#    estatua_id = models.IntegerField(null=True)
#    tipo_interaccion = models.CharField(max_length=100, null=True)
#    fecha_interaccion = models.DateTimeField(null=True)
#    duracion_interaccion = models.IntegerField(null=True)
#    informacion_adicional = models.TextField(null=True)

#class Mapa(models.Model):
#    nombre = models.CharField(max_length=255, null=True)

#class RealidadAumentada(models.Model):
#    estatua = models.ForeignKey('Estatuas', on_delete=models.SET_NULL, null=True)
#    modelo_3d_ar = models.TextField(null=True)
#    funcionalidades_ar = models.TextField(null=True)

#class Ruta(models.Model):
#    nombre = models.CharField(max_length=255, null=True)
#    descripcion = models.TextField(null=True)
#    mapa = models.ForeignKey('Mapa', on_delete=models.SET_NULL, null=True)

#class Usuario(models.Model):
#    nombre = models.CharField(max_length=255, null=True)
#    motivo_de_uso = models.CharField(max_length=255, null=True)
#    idioma_preferido = models.CharField(max_length=100, null=True)
#    dispositivo = models.ForeignKey('DispositivoMovil', on_delete=models.SET_NULL, null=True)

class EstatuaSimplificada(models.Model):
   nombre = models.CharField(max_length=255, null=True)
   id = models.IntegerField(primary_key=True)
   descripcion = models.TextField(null=True)
   modelo = models.FileField(upload_to='modelos/')
   ubicacion = models.TextField(null=True)