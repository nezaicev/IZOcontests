import os.path

from sorl.thumbnail import get_thumbnail
from django.conf import settings
from rest_framework import serializers
from .models import ModxDbimgMuz, Archive, Level, ExtraImageArchive, \
    NominationVP, DirectionVP, VideoArchive, FileArchive, Region, ThemeART, \
    ThemeRUSH, NominationMYMSK
from contests.utils import upload_file, parse_path_file, download_file


class ModxDbimgMuzSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModxDbimgMuz
        fields = ('id', 'oldname', 'material')


class NominationVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = NominationVP
        fields = ('name',)


class NominationMymoskvichiSerializer(serializers.ModelSerializer):
    class Meta:
        model = NominationMYMSK
        fields = ('name',)


class ThemeArtakiadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeART
        fields = ('name',)


class ThemeNRushevaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeRUSH
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
                    }
        else:
            return None


class RegionSerializer(serializers.RelatedField):
    class Meta:
        model = Region

    def to_representation(self, value):
        return value.name


class YearContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive

    def to_representation(self, instance):
        return {
            'years': (),
        }


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


class CustomImageField(serializers.Field):

    def to_internal_value(self, data):
        file = parse_path_file(data)
        if file['http']:
            downloaded_path_file = download_file(file['path'],
                                                 file['file_name'],
                                                 file['extension'])

            if os.path.exists(downloaded_path_file):
                return upload_file(downloaded_path_file,
                                   settings.PATH_IMG_UPLOAD, file['extension'])
        else:
            if os.path.exists(file['path']):
                return upload_file(file['path'], settings.PATH_IMG_UPLOAD,
                                   file['extension'])

        if 'http' not in data:
            return upload_file(data, settings.PATH_IMG_UPLOAD,
                               file['extension'])

    def get_attribute(self, instance):
        return instance

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
                    }
        else:
            return None


class ArchiveSerializer(serializers.ModelSerializer):
    reg_number = serializers.CharField(required=True)
    image = CustomImageField()
    images = ImagesSerializer(many=True, read_only=True)
    videos = VideosSerializer(many=True, read_only=True)
    files = FilesSerializer(many=True, read_only=True)
    region = RegionSerializer(many=False, read_only=True)

    class Meta:
        model = Archive
        fields = ('id', 'reg_number',
                  'link', 'author_name', 'fio', 'fio_teacher', 'school',
                  'contest_name', 'image', 'publish',
                  'nomination', 'level', 'age', 'status', 'material',
                  'description', 'theme',
                  'direction', 'images', 'videos', 'files', 'region', 'city',
                  'rating', 'year_contest')

    def create(self, validated_data):
        return Archive.objects.create(**validated_data)
