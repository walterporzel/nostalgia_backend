from rest_framework import serializers
from .models import Decade,Fad

class DecadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Decade
       fields = ('id', 'start_year')

class FadSerializer(serializers.HyperlinkedModelSerializer):
    decade = serializers.HyperlinkedRelatedField(
        view_name='start_year',
        read_only=True
    )
    class Meta:
        model = Fad
        fields = ('id', 'name', 'img_url', 'description', 'decade')