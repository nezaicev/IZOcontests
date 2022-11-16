from rest_framework import serializers
from content.models import Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('slug', 'title', 'subtitle', 'content')
