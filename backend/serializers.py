from rest_framework import serializers
from .models import Evident


class EvidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evident
        fields = '__all__'
