from rest_framework import serializers

from .models import CMS


class CMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMS
        read_only_fields = (
            'created_at',
        ),
        fields = (
            'id',
            'name',
            'phone',
            'email',
            'created_at',
        )
