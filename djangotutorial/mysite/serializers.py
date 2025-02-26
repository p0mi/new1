from rest_framework import serializers

class RouteSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    url = serializers.CharField(max_length=255)
    pattern = serializers.CharField(max_length=255)