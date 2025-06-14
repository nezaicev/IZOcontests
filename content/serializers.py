from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from content.models import Page, Video, Category, Publication
from utils import extract_rutube_id, get_rutube_thumbnail


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('slug', 'title', 'subtitle', 'content')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def to_representation(self, value):
        return value.name


class VideoSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ['link', 'title', 'categories', 'order','description']
        # fields = '__all__'

    def to_representation(self, value):
        data = {'link': value.link,
                'name': value.title,
                'description': value.description,
                'categories': CategorySerializer(value.categories.all(), many=True).data,
                'orderNumber': value.order}
        link = data.get("link", "")
        if link:
            if "rutube" in link:
                video_id = extract_rutube_id(link)
                if video_id:
                    poster_url = get_rutube_thumbnail(video_id)
                    if poster_url:
                        data["poster"] = poster_url  # Добавляем в вывод

        return data


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
