from django.db import models


class Camera(models.Model):
    url = models.CharField(max_length=600)


class Slice(models.Model):
    shape = models.CharField(max_length=600)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=150, blank=True)
    cameras = models.ManyToManyField(Camera)
    slices = models.ManyToManyField(Slice)


class Event(models.Model):
    name = models.CharField(max_length=150, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Statistic(models.Model):
    timestamp = models.DateTimeField()
    state = models.BooleanField()


class Model(models.Model):
    slices = models.ForeignKey(Slice, on_delete=models.CASCADE, blank=True)
    statistics = models.ManyToManyField(Statistic, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Image(models.Model):
    path = models.CharField(max_length=500)
    file_name = models.CharField(max_length=150)
    active = models.BooleanField()
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
