from rest_framework import serializers
from .models import ModxDbimgMuz, Archive, Level


class ModxDbimgMuzSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModxDbimgMuz
        fields = ('id', 'oldname', 'material')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('name',)


class ArchiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Archive
        fields = (
            'link', 'author_name', 'fio', 'contest_name', 'image',
            'nomination', 'level', 'status')
