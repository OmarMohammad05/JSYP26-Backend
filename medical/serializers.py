from rest_framework import serializers

class OCRSerializer(serializers.Serializer):
    image=serializers.ImageField()

class TextSerializer(serializers.Serializer):
    text=serializers.CharField()