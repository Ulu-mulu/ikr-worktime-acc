from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, mixins
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Camera, Tag, Image
from .serializers import *

class CameraViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet
    ):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ImageViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet
    ):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class StatisticViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet
    ):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer

    @action(detail=False, methods=['GET'])
    def between_timestamps(self, request):
        ts_start = request.query_params.get('ts_start')
        ts_end = request.query_params.get('ts_end')
        if ts_start is None and ts_end is None:
            statistic = Statistic.objects.all()
        elif ts_start is None:
            statistic = Statistic.objects.filter(timestamp__lte=ts_end)
        elif ts_end is None:
            statistic = Statistic.objects.filter(timestamp__gte=ts_start)
        else:
            statistic = Statistic.objects.filter(
                timestamp__range=(ts_start, ts_end)
            )
        serializer = StatisticSerializer(statistic, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ModelViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet
    ):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class SliceViewSet(viewsets.ModelViewSet):
    queryset = Slice.objects.all()
    serializer_class = SliceSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
