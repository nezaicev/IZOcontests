from rest_framework import serializers
from content.models import Page, Video, Category


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('slug', 'title', 'subtitle', 'content')


class CategorySerializer(serializers.RelatedField):
    class Meta:
        model = Category

    def to_representation(self, value):
        return value.name


class VideoSerializer(serializers.ModelSerializer):
    categories=CategorySerializer(many=True, read_only=True)
    # images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'
