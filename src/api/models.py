from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()

class Fish(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    speed = models.IntegerField()