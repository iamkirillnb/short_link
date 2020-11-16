from random import randint, choice

from rest_framework import serializers
from .models import Links




class LinksSerializer(serializers.Serializer):
    link = serializers.URLField()

    def create(self, validated_data):
        return Links.objects.create(**validated_data)
