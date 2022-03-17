from sorl.thumbnail import get_thumbnail

from rest_framework import serializers
from .models import ModxDbimgMuz, Archive, Level, ExtraImageArchive, \
    NominationVP, DirectionVP


class ModxDbimgMuzSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModxDbimgMuz
        fields = ('id', 'oldname', 'material')


class NominationVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = NominationVP
        fields = ('name',)


class DirectionVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionVP
        fields = ('name',)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('name',)


class ImagesSerializer(serializers.RelatedField):
    model = ExtraImageArchive

    def to_representation(self, value):
        return {'thumb': get_thumbnail(value.image, '300x300', crop='center',
                                       quality=99).url,
                'original': value.image.url}


class ArchiveSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Archive

        fields = ('id', 'reg_number',
                  'link', 'author_name', 'fio', 'fio_teacher', 'school',
                  'contest_name', 'image',
                  'nomination', 'level', 'status', 'images', 'description',
                  'direction')
