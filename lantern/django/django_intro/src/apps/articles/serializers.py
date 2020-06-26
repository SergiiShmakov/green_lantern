from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=5000)
    tags = serializers.CharField(max_length=32)
    author = serializers.CharField(max_length=32)
