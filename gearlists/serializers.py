from rest_framework import serializers
from .models import GearList


class GearListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    gearitem_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = GearList
        fields = fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'title', 'description', 'image',
            'category', 'gearitem_count',
        ]
