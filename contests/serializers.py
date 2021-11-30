from rest_framework import serializers
from .models import ModxDbimgMuz


class ModxDbimgMuzSerializer(serializers.ModelSerializer):
    class Meta:
        model=ModxDbimgMuz
        fields=('id','oldname','material')