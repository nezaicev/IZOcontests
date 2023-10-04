from abc import ABC

from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from contests.models import ExtraImageArchive
from exposition.models import Exposition, ImageExposition, Comment


#
# class CommentField(serializers.RelatedField, ABC):
#     class Meta:
#         model = Comment
#         fields = ("author", "content", "exposition", "created")


class CommentsListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(publication_status='p')
        return super(CommentsListSerializer, self).to_representation(data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = CommentsListSerializer
        model = Comment
        fields = ("author", "content", "exposition")

    # def to_representation(self, instance):
    #     if instance.publication_status == 'p':
    #         return instance


class ImagesExpositionSerializer(serializers.RelatedField):
    class Meta:
        model = ImageExposition

    def to_representation(self, value):
        crop_orientation = 'center'
        if value.crop_orientation_img:
            crop_orientation = value.crop_orientation_img
        if value.image:
            return {'thumb': get_thumbnail(value.image.url, '320x320',
                                           crop=crop_orientation,
                                           quality=99).url,
                    'md_thumb': get_thumbnail(value.image.url, '2000',
                                              quality=99).url,
                    'original': value.image.url,
                    'label': value.label
                    }
        else:
            return None


class PosterExpositionField(serializers.Field):

    def to_representation(self, value):

        if value:
            return {'thumb': get_thumbnail(value.url, 'x400',
                                           quality=99).url,
                    'original': value.url,
                    }
        else:
            return None


class ExpositionSerializer(serializers.ModelSerializer):
    poster = PosterExpositionField()
    comments = CommentSerializer(many=True, read_only=True)
    images = ImagesExpositionSerializer(many=True, read_only=True)

    class Meta:
        model = Exposition
        fields = ('__all__')


class ExpositionListSerializer(serializers.ModelSerializer):
    poster = PosterExpositionField()

    class Meta:
        model = Exposition
        fields = (
            'id', 'title', 'poster', 'start_date', 'end_date', 'address', 'count_participants',
            'count_exp', 'publicate', 'virtual')


class YearExpositionField(serializers.Field):

    def to_representation(self, value):

        if value:
            return {'year': value.year}
        else:
            return None


class YearsExpositionSerializer(serializers.ModelSerializer):
    start_date = YearExpositionField()

    class Meta:
        model = Exposition
        fields = ('start_date')
