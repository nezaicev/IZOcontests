from sorl.thumbnail import get_thumbnail

from rest_framework import serializers
from .models import ModxDbimgMuz, Archive, Level, ExtraImageArchive, \
<<<<<<< HEAD
    NominationVP, DirectionVP, VideoArchive, FileArchive, Region, ThemeART, ThemeRUSH, NominationMYMSK
=======
    NominationVP, DirectionVP, VideoArchive, FileArchive, Region, ThemeART, \
    ThemeRUSH, Artakiada, NRusheva
>>>>>>> frontend


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
        return {'thumb': get_thumbnail(value.image, '320x180', crop='center',
                                       quality=99).url,
                'md_thumb': get_thumbnail(value.image, '2000',
                                          quality=99).url,
                'original': value.image.url,
                'orderNumber': value.order_number}


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


class ThumbnailSerializer(serializers.ImageField):

    def to_representation(self, value):
        if value:
            return {'thumb': get_thumbnail(value.url, '320x180', crop='center',
                                           quality=99).url,
                    'md_thumb': get_thumbnail(value.url, '1152',
                                              quality=99).url,
                    'original': value.url,
                    }
        else:
            return {}


class ArchiveSerializer(serializers.ModelSerializer):
    image = ThumbnailSerializer()
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
