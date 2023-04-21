from rest_framework import serializers

from characters.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "api_id", "name", "status", "species", "gender", "image")
