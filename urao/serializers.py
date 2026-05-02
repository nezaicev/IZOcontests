from rest_framework import serializers
from sorl.thumbnail import get_thumbnail
from urao.models import ProfileURAO, Image


class ProfileURAOListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    avatar_thumb = serializers.SerializerMethodField()
    works_count = serializers.SerializerMethodField()

    class Meta:
        model = ProfileURAO
        fields = ('id', 'full_name', 'avatar_thumb', 'year_graduation', 'works_count')

    def get_full_name(self, obj):
        if obj.user:
            return f"{obj.user.fio}".strip()
        return ""

    def get_avatar_thumb(self, obj):
        if obj.avatar:
            try:
                return get_thumbnail(obj.avatar.url, '200x200', crop='center', quality=99).url
            except Exception:
                # Если не удалось создать миниатюру, возвращаем оригинал
                return obj.avatar.url
        return None

    def get_works_count(self, obj):
        return obj.images.count()


class ImageURAOSerializer(serializers.ModelSerializer):
    image_thumb = serializers.SerializerMethodField()
    image_md = serializers.SerializerMethodField()
    image_original = serializers.SerializerMethodField()
    material_name = serializers.CharField(source='material.name', read_only=True)

    class Meta:
        model = Image
        fields = (
            'id', 'author_name', 'image_thumb', 'image_md', 'image_original',
            'material_name', 'year', 'size'
        )

    def get_image_thumb(self, obj):
        if obj.image:
            try:
                return get_thumbnail(obj.image.url, '320x320', crop='center', quality=99).url
            except Exception:
                return obj.image.url
        return None

    def get_image_md(self, obj):
        if obj.image:
            try:
                return get_thumbnail(obj.image.url, '2000', quality=99).url
            except Exception:
                return obj.image.url
        return None

    def get_image_original(self, obj):
        if obj.image:
            return obj.image.url
        return None


class ProfileURAODetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    avatar_thumb = serializers.SerializerMethodField()
    images = ImageURAOSerializer(many=True, read_only=True)

    class Meta:
        model = ProfileURAO
        fields = ('id', 'full_name', 'avatar_thumb', 'bio', 'year_graduation', 'images')

    def get_full_name(self, obj):
        if obj.user:
            return f"{obj.user.fio}".strip()
        return ""

    def get_avatar_thumb(self, obj):
        if obj.avatar:
            try:
                return get_thumbnail(obj.avatar.url, '300x300', crop='center', quality=99).url
            except Exception:
                # Если не удалось создать миниатюру, возвращаем оригинал
                return obj.avatar.url
        return None