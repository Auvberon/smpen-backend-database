from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import user, inventory, logging
from .serializers import userSerializer, inventorySerializer, loggingSerializer

class userView(APIView):
    def get(self, request):
        users = user.objects.all()
        serializer = userSerializer(users, many=True)
        return Response({"user" : serializer.data})

    def post(self, request):
        users = request.data.get('user')
        serializer = userSerializer(data=users)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.uname)})

    # def put(self, request, update_user_pk):
    #     saved_user = get_object_or_404(user.objects.all(), pk=update_user_pk)
    #     data = request.data.get('user')
    #     serializer = userSerializer(instance=saved_user, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         user_saved = serializer.save()
    #     return Response({"success": "User '{}' updated successfully".format(user_saved.uname)})

    # def delete(self, request, delete_user_pk):
    #     # Get object with this pk
    #     users = get_object_or_404(user.objects.all(), pk=delete_user_pk)
    #     users.delete()
    #     return Response({"message": "User with id `{}` has been deleted.".format(delete_user_pk)},status=204)

class inventoryView(APIView):
    def get(self, request):
        inventories = inventory.objects.all()
        serializer = inventorySerializer(inventories, many=True)
        return Response({"Inventory" : serializer.data})

    def post(self, request):
        inventories = request.data.get('inventory')
        serializer = inventorySerializer(data=inventories)
        if serializer.is_valid(raise_exception=False):
            inventory_saved = serializer.save()
            return Response({"success": "Item '{}' created successfully".format(inventory_saved.name)})

    def put(self, request, uid):
        saved_inventory = get_object_or_404(inventory.objects.all(), pk=uid)
        data = request.data.get('inventory')
        serializer = inventorySerializer(instance=saved_inventory, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            inventory_saved = serializer.save()
        return Response({"success": "UID {}'s name updated successfully to {}".format(inventory_saved.uid, inventory_saved.name)})

class loggingView(APIView):
    def get(self, request):
        loggings = logging.objects.all()
        serializer = loggingSerializer(loggings, many=True)
        return Response({"Logging" : serializer.data})