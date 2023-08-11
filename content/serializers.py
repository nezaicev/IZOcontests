from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from content.models import Page, Video, Category, Publication


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
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'


class PosterPublicationField(serializers.Field):

    def to_representation(self, value):

        if value:
            return {'thumb': get_thumbnail(value.url, 'x400',
                                           quality=99).url,
                    'original': value.url,
                    }
        else:
            return None


class PublicationSerializer(serializers.ModelSerializer):
    poster = PosterPublicationField()

    class Meta:
        model = Publication
        fields = '__all__'
