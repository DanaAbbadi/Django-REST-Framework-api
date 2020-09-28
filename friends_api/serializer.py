from rest_framework import serializers

from .models import Friends

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','character','line', 'plot', 'episode', 'season')
        model = Friends