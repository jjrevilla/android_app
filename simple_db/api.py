from .models import Articulo, Pedido
from .serializers import ArticuloSerializer, PedidoSerializer

from django.http import Http404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

class ArticuloList(APIView):
    def get(self, request, format=None):
        articulos = Articulo.objects.all()
        serialized_articulos = ArticuloSerializer(articulos, many=True)       
        return Response(serialized_articulos.data)
    
    def post(self, request, format=None):
        serialized_articulo = ArticuloSerializer(data=request.data)
        if serialized_articulo.is_valid():
            serialized_articulo.save()
            return Response(serialized_articulo.data, status=status.HTTP_201_CREATED)
        return Response(serialized_articulo.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticuloDetail(APIView):
    def get_object(self, pk):
        try:
            return Articulo.objects.get(id=pk)
        except Articulo.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        articulo = self.get_object(pk)
        serialized_articulo = ArticuloSerializer(articulo)
        return Response(serialized_articulo.data)

    def put(self, request, pk, format=None):
        articulo = self.get_object(pk)
        serialized_articulo = ArticuloSerializer(articulo)
        if serialized_articulo.is_valid():
            serialized_articulo.save()
            return Response(serialized_articulo.data)
        return Response(serialized_articulo.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        serialized_articulo = self.get_object(pk)
        serialized_articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PedidoList(APIView):
    def get(self, request, format=None):
        pedidos = Pedido.objects.all()
        serialized_pedidos = PedidoSerializer(pedidos, many=True)
        return Response(serialized_pedidos.data)

    def post(self, request, format=None):
        serialized_pedido = PedidoSerializer(data=request.data)
        if serialized_pedido.is_valid():
            serialized_pedido.save()
            return Response(serialized_pedido.data, status=status.HTTP_201_CREATED)
        return Response(serialized_pedido.errors, status=status.HTTP_400_BAD_REQUEST)


class PedidoDetail(APIView):
    def get_object(self, pk):
        try:
            return Pedido.objects.get(pk=pk)
        except Pedido.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        pedido = self.get_object(pk)
        serialized_pedido = PedidoSerializer(pedido)
        return Response(serialized_pedido.data)


    def put(self, request, pk, format=None):
        pedido = self.get_object(pk)
        serialized_pedido = PedidoSerializer(articulo)
        if serialized_pedido.is_valid():
            serialized_pedido.save()
            return Response(serialized_pedido.data)
        return Response(serialized_pedido.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        serialized_pedido = self.get_object(pk)
        serialized_pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
