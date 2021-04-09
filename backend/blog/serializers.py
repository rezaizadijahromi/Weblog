from rest_framework import serializers
from .models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['author', 'category', 'title', 'description', 'cover', 'created', 'updated']


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
