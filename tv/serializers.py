from rest_framework import serializers
from .models import Trending, Details, Cast, Video

class TrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trending
        fields = '__all__'

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'