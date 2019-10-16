from rest_framework import serializers
from .models import Decade,Fad

class DecadeSerializer(serializers.ModelSerializer):

    class Meta:
       model = Decade
       fields = ('id', 'start_year')

class FadSerializer(serializers.ModelSerializer):
    decade = serializers.StringRelatedField()

    class Meta:
        model = Fad
        fields = ('id', 'name', 'img_url', 'description', 'decade')