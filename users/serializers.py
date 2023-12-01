from rest_framework import serializers


class UserLoginRegisterSerializer(serializers.Serializer):
    """Serialization / Deserialization data for Users Registration and Login"""

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
