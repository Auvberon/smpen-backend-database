from rest_framework import serializers

from .models import logging, inventory

from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'user_permissions')

class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')


class inventoryQtySerializer(serializers.Serializer):
    qty = serializers.IntegerField()

class inventoryDetailSerializer(serializers.Serializer):
    logical_uid = serializers.CharField(max_length = 50)
    name = serializers.CharField(max_length = 50)
    qty = serializers.IntegerField()

class inventorySerializer(serializers.Serializer):
    logical_uid = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    qty = serializers.IntegerField()

    def create(self, validated_data):
        return inventory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.logical_uid = validated_data.get('logical_uid', instance.logical_uid)
        instance.name = validated_data.get('name', instance.name)
        instance.qty = validated_data.get('qty', instance.qty)

        instance.save()
        return instance

class loggingSerializer(serializers.ModelSerializer):
    # logical_uid = serializers.CharField(max_length=50)
    # logical_uid = serializers.RelatedField(source='Inventory', read_only=True)
    logicaluid = serializers.RelatedField(source='logical_uid', read_only=True)
    status = serializers.CharField(max_length=144)
    qty = serializers.IntegerField()
    time = serializers.CharField(max_length = 144)
    warehouse = serializers.CharField(max_length = 144)

    class Meta:
        model = logging
        fields = "__all__"

    def create(self, validated_data):
        return logging.objects.create(**validated_data)