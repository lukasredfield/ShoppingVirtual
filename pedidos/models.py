from django.db import models

from django.contrib.auth import get_user_model

from tienda.models import Productos

from django.db.models import F, Sum, FloatField 

# Create your models here.

User=get_user_model()

class Pedido(models.Model):


    user=models.ForeignKey(User, on_delete=models.CASCADE)  # type: ignore
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id  # type: ignore

    @property
    def total(self):
        return self.lineapedido_set.aggregate()  # type: ignore

        total=Sum(F("precio")*F("cantidad"), output_field=FloatField())["total"]

    class Meta:
        db_table='pedidos'  #cómo se va a llamar la tabla en la base de datos
        verbose_name= 'pedido'
        verbose_name_plural= 'pedidos'
        ordering=['id']

class LineaPedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)  # type: ignore
    producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        db_table='lineapedidos'  #cómo se va a llamar la tabla en la base de datos
        verbose_name= 'Línea pedido'
        verbose_name_plural= 'Líneas pedidos'
        ordering=['id']


