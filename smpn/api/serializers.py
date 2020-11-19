from rest_framework import serializers

from .models import user, inventory, logging

class userSerializer(serializers.Serializer):
    uname = serializers.CharField(max_length=144)
    passwd = serializers.CharField(max_length=144)
    permission = serializers.CharField(max_length=144)

    def create(self, validated_data):
        return user.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.uname = validated_data.get('uname', instance.uname)
        instance.passwd = validated_data.get('passwd', instance.passwd)
        instance.permission = validated_data.get('permission', instance.permission)

        instance.save()
        return instance

class inventorySerializer(serializers.Serializer):
    logical_uid = serializers.CharField(max_length = 50)
    name = serializers.CharField(max_length = 50)
    qty = serializers.IntegerField()

    def create(self, validated_data):
        return inventory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.logical_uid = validated_data.get('logical_uid', instance.logical_uid)
        instance.name = validated_data.get('name', instance.name)
        instance.qty = validated_data.get('qty', instance.qty)

        instance.save()
        return instance

class loggingSerializer(serializers.Serializer):
    logical_uid = serializers.CharField(max_length = 50)
    status = serializers.CharField(max_length = 50)
    qty = serializers.IntegerField()
    time = serializers.CharField(max_length = 144)