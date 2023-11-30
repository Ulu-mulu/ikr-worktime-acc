from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Camera, Tag, Image
from .serializers import *

class CameraList(APIView):
    def get(self, request, format=None):
        cameras = Camera.objects.all()
        serializer = CameraSerializer(cameras, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = CameraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CameraDetailed(APIView):

    def get_object(self, pk):
        try:
            return Camera.objects.get(pk=pk)
        except Camera.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        camera = self.get_object(pk)
        serializer = CameraSerializer(camera)
        return Response(serializer.data)
    

    def delete(self, request, pk, format=None):
        camera = self.get_object(pk)
        camera.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagList(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagDetailed(APIView):

    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)
    

    def put(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        tag = self.get_object(pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageList():
    def get(self, request, format=None):
        tags = Image.objects.all()
        serializer = ImageSerializer(tags, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ImageDetailed():
    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = ImageSerializer(tag)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        tag = self.get_object(pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StatisticsList():
    def get(self, request, format=None):
        tags = Statistic.objects.all()
        serializer = StatisticSerializer(tags, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = StatisticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatisticDetailed():
    def get_object(self, timestamp_start, timestamp_end):
        try:
            query = Statistic.objects.filter(
                timestamp__range=(timestamp_start, timestamp_end)
            )
            return query
        except Image.DoesNotExist:
            raise Http404


    def get(self, request, timestamp_start, timestamp_end, format=None):
        tag = self.get_object(timestamp_start, timestamp_end)
        serializer = ImageSerializer(tag)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        tag = self.get_object(pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
