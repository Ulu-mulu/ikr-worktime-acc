from django.db import models

class Cameras(models.Model):
    pass

class Slices(models.Model):
    camera = models.ForeignKey(Cameras, on_delete=models.CASCADE)

class Tags(models.Model):
    cameras = models.ManyToManyField(Cameras)
    slices = models.ManyToManyField(Slices)

class Events(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

class Statistics(models.Model):
    pass

class Models(models.Model):
    slices = models.ForeignKey(Slices, on_delete=models.CASCADE)
    statistics = models.ManyToManyField(Statistics)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

class Images(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE)
