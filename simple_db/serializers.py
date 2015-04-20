from .models import Articulo, Pedido
from rest_framework import serializers

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('id','articulo','stock','costo',)


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id','codigo_articulo','cantidad','costo',)
