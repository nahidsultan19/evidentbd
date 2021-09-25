from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Evident
from .serializers import EvidentSerializer


@api_view(['GET'])
def apiView(request):
    api_list = {
        'List': '/list/',
        'Create': '/create/',
        'Update': '/update/<str:pk>/',
        'Detail': '/detail/<str:pk>/',
        'Delete': '/delete/<str:pk>/'
    }
    return Response(api_list)


@api_view(['GET'])
def List(request):
    evident = Evident.objects.all()
    serializer = EvidentSerializer(evident, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def Create(request):
    serializer = EvidentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def Update(request, pk):
    evident = Evident.objects.get(id=pk)
    serializer = EvidentSerializer(instance=evident, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def Detail(request, pk):
    evident = Evident.objects.get(id=pk)
    serializer = EvidentSerializer(evident, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def Delete(request, pk):
    evident = Evident.objects.get(id=pk)
    evident.delete()
    return Response('Item SuccessFully Deleted!')
