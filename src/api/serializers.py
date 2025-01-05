from rest_framework import serializers
from api.models import Fish, Plant


class FishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fish
        fields = ["id", "url", "name", "speed", "image_url"]


class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ["id", "url", "name", "image_url"]
