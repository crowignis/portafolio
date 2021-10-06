# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    idadmin = models.AutoField(primary_key=True)
    nombreadmin = models.CharField(max_length=30, blank=True, null=True)
    passadmin = models.CharField(max_length=30, blank=True, null=True)
    fechaingreso = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrador'


class Cliente(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    nombrecliente = models.CharField(max_length=30, blank=True, null=True)
    mesa_idmesa = models.ForeignKey('Mesa', models.DO_NOTHING, db_column='mesa_idmesa')

    class Meta:
        managed = False
        db_table = 'cliente'


class Compra(models.Model):
    idcompra = models.IntegerField(primary_key=True)
    fechacompra = models.DateField(blank=True, null=True)
    horacompra = models.DateField(blank=True, null=True)
    solicitud_insumos_idsolicitud = models.ForeignKey('SolicitudInsumos', models.DO_NOTHING, db_column='solicitud_insumos_idsolicitud')
    solicitud_insumos_administrador_idadmin = models.ForeignKey('SolicitudInsumos', related_name='solicitudadmin', on_delete=models.DO_NOTHING ,db_column='solicitud_insumos_administrador_idadmin')
    valorcompra = models.BigIntegerField(blank=True, null=True)
    finanzas_finanzas = models.ForeignKey('Finanzas', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'compra'


class Finanzas(models.Model):
    idfinanzas = models.BigIntegerField(blank=True, null=True)
    ingresos = models.BigIntegerField(blank=True, null=True)
    egresos = models.BigIntegerField(blank=True, null=True)
    finanzas_id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'finanzas'


class Mesa(models.Model):
    idmesa = models.FloatField(primary_key=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    disponibilidad = models.CharField(max_length=1, blank=True, null=True)
    nromesa = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesa'


class Producto(models.Model):
    idproducto = models.FloatField(primary_key=True)
    descripcionproducto = models.CharField(max_length=30, blank=True, null=True)
    solicitud_insumos_idsolicitud = models.ForeignKey('SolicitudInsumos', models.DO_NOTHING, db_column='solicitud_insumos_idsolicitud')
    cantidad = models.BigIntegerField(blank=True, null=True)
    solicitud_insumos_administrador_idadmin = models.ForeignKey('SolicitudInsumos', related_name='solicitudInsuAdmin', on_delete= models.DO_NOTHING, db_column='solicitud_insumos_administrador_idadmin')
    bodega_idproducto = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'producto'
        unique_together = (('idproducto', 'solicitud_insumos_idsolicitud', 'solicitud_insumos_administrador_idadmin', 'bodega_idproducto'),)


class Proveedor(models.Model):
    idproveedor = models.BigIntegerField(primary_key=True)
    nombreproveedor = models.CharField(max_length=30, blank=True, null=True)
    correoproveedor = models.CharField(max_length=30, blank=True, null=True)
    idsolicitud = models.FloatField()
    idadmin = models.FloatField()

    class Meta:
        managed = False
        db_table = 'proveedor'


class Receta(models.Model):
    idreceta = models.IntegerField(primary_key=True)
    nombrereceta = models.CharField(max_length=300, blank=True, null=True)
    valorreceta = models.IntegerField(blank=True, null=True)
    bodega_idproducto = models.CharField(max_length=6)
    pedido_idpedido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'receta'
        unique_together = (('idreceta', 'bodega_idproducto', 'pedido_idpedido'),)


class SolicitudInsumos(models.Model):
    idsolicitud = models.IntegerField(primary_key=True)
    iddetallesolicitud = models.CharField(max_length=300, blank=True, null=True)
    administrador_idadmin = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador_idadmin')
    proveedor_idproveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='proveedor_idproveedor')

    class Meta:
        managed = False
        db_table = 'solicitud_insumos'
        unique_together = (('idsolicitud', 'administrador_idadmin'),)


class Venta(models.Model):
    idventa = models.IntegerField(primary_key=True)
    fechaventa = models.DateField(blank=True, null=True)
    horaventa = models.DateField(blank=True, null=True)
    pedido_idpedido = models.IntegerField()
    valorventa = models.FloatField(blank=True, null=True)
    finanzas_finanzas = models.ForeignKey(Finanzas, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'venta'
