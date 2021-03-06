# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import json
from django.db import models


class Bodega(models.Model):
    id_bodega = models.BigIntegerField(primary_key=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    stock = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bodega'


class Cliente(models.Model):
    id_cliente = models.BigIntegerField(primary_key=True)
    nombre_cliente = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cliente'


class Cocina(models.Model):
    id_cocina = models.BigIntegerField(primary_key=True)
    id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='id_pedido')
    id_estado_pedido = models.ForeignKey('EstadoPedido', models.DO_NOTHING, db_column='id_estado_pedido')

    class Meta:
        managed = False
        db_table = 'cocina'





class EstadoPedido(models.Model):
    id_estado_pedido = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class Finanzas(models.Model):
    id_finanza = models.BigIntegerField(primary_key=True)
    id_pedido_producto = models.ForeignKey('PedidoProducto', models.DO_NOTHING, db_column='id_pedido_producto')
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'finanzas'


class Mesas(models.Model):
    id_mesa = models.BigIntegerField(primary_key=True)
    disponibilidad = models.CharField(max_length=1)
    estado_reserva = models.CharField(max_length=1)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    numero_mesa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mesas'


class Pedido(models.Model):
    id_pedido = models.BigIntegerField(primary_key=True)
    id_mesa = models.ForeignKey(Mesas, models.DO_NOTHING, db_column='id_mesa')
    fecha_pedido = models.DateField()
    precio_total = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoProducto(models.Model):
    id_pedido_producto = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pedido_producto'


class PedidosProductoIntermedio(models.Model):
    id_producto_intermedio = models.BigIntegerField(primary_key=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    id_pedido_producto = models.ForeignKey(PedidoProducto, models.DO_NOTHING, db_column='id_pedido_producto')
    cantidad_producto = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedidos_producto_intermedio'


class ProductoReceta(models.Model):
    id_producto_receta = models.BigIntegerField(primary_key=True)
    id_receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='id_receta')
    id_producto = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='id_producto')
    cantidad_producto = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'producto_receta'


class Productos(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    nombre_producto = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'productos'
    
    def json_serializer(self):
        return {
                    'id_producto': self.id_producto,
                    'id_proveedor': self.id_proveedor.json_serializer(),
                    'nombre_producto': self.nombre_producto,
                    'descripcion': self.descripcion,
                   
                    
        }


class Proveedor(models.Model):
    id_proveedor = models.BigIntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=30, blank=True, null=True)
    apellido_proveedor = models.CharField(max_length=20)
    rut_proveedor = models.CharField(max_length=12)
    contacto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'proveedor'
    
    def json_serializer(self):
        return {
                    'id_proveedor': self.id_proveedor,
                    'nombre_proveedor': self.nombre_proveedor,
                    'apellido_proveedor': self.apellido_proveedor,
                    'rut_proveedor': self.rut_proveedor,
                    'contacto': self.contacto
                    
        }

    


class Receta(models.Model):

    id_receta = models.BigIntegerField(primary_key=True)
    precio = models.BigIntegerField()
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'receta'
    
    def json_serializer(self):
        return {
                    'id_receta': self.id_receta,
                    'precio': self.precio,
                    'nombre': self.nombre,
                    'descripcion': self.descripcion
        }


class RecetaPedido(models.Model):
    id_receta_pedido = models.BigIntegerField(primary_key=True)
    id_receta = models.ForeignKey(Receta, models.DO_NOTHING, db_column='id_receta')
    id_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido')
    cantidad_receta = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'receta_pedido'


class Rol(models.Model):
    id_rol = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'rol'


class UsuarioRol(models.Model):
    id_usuario_rol = models.BigIntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol')

    class Meta:
        managed = False
        db_table = 'usuario_rol'


class Usuarios(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=10)
    contrasena = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'usuarios'
