from rest_framework import serializers


class DialoguesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    bot_id = serializers.ListField(child=serializers.IntegerField())
