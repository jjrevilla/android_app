from django.db import models

class Articulo(models.Model):
    id = models.IntegerField(primary_key=True, max_length=5)
    articulo = models.TextField(max_length=20)
    stock = models.IntegerField()
    costo = models.FloatField(max_length=10)
    
    def __str__(self):
        return self.articulo

    class Meta:
        verbose_name_plural = "Articulos"



class Pedido(models.Model):
    id = models.IntegerField(primary_key=True, max_length=5)
    codigo_articulo = models.ForeignKey(Articulo)
    cantidad = models.IntegerField()
    costo = models.FloatField(max_length=10)

    def __str__(self):
        return str(self.codigo_articulo)


    class Meta:
        verbose_name_plural = "Pedidos"
