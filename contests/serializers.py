from sorl.thumbnail import get_thumbnail

from rest_framework import serializers
from .models import ModxDbimgMuz, Archive, Level, ExtraImageArchive, \
    NominationVP, DirectionVP, VideoArchive, FileArchive, Region


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
    class Meta:
        model = ExtraImageArchive

    def to_representation(self, value):
        return {'thumb': get_thumbnail(value.image, '320x180', crop='center',
                                       quality=99).url,
                'original': value.image.url,
                'orderNumber': value.order_number}

class RegionSerializer(serializers.RelatedField):
    class Meta:
        model = Region

    def to_representation(self, value):
        return value.name




class VideosSerializer(serializers.RelatedField):
    class Meta:
        model = VideoArchive

    def to_representation(self, value):
        return {'link': value.video,
                'name': value.name,
                'orderNumber': value.order_number}


class FilesSerializer(serializers.RelatedField):
    class Meta:
        model = FileArchive

    def to_representation(self, value):
        return {'name': value.name,
                'link': value.file.url,
                }


class ArchiveSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)
    videos = VideosSerializer(many=True, read_only=True)
    files=FilesSerializer(many=True, read_only=True)
    region=RegionSerializer(many=False, read_only=True)

    class Meta:
        model = Archive

        fields = ('id', 'reg_number',
                  'link', 'author_name', 'fio', 'fio_teacher', 'school',
                  'contest_name', 'image', 'publish',
                  'nomination', 'level', 'age', 'status',
                  'description',
                  'direction', 'images','videos', 'files', 'region', 'city')
