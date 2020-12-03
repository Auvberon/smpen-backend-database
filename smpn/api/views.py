from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import permissions, status
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view

from .models import logging, inventory
from .serializers import loggingSerializer, inventorySerializer, inventoryQtySerializer, inventoryDetailSerializer, UserSerializer, UserSerializerWithToken,loggingSerializerGet

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"user" : serializer.data})

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class inventoryQty(APIView):
    def get_object(self, get_uid):
        try:
            return inventory.objects.get(pk=get_uid)
        except inventory.DoesNotExist:
            raise Http404

    def get(self, request, get_uid, format=None):
        snippet = self.get_object(get_uid)
        serializer = inventoryQtySerializer(snippet)
        return Response(serializer.data)

class inventoryDetail(APIView):
    def get_object(self, detailed_uid):
        try:
            return inventory.objects.get(pk=detailed_uid)
        except inventory.DoesNotExist:
            raise Http404("Item not yet exist")

    def get(self, request, detailed_uid, format=None):
        snippet = self.get_object(detailed_uid)
        serializer = inventoryDetailSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, logical_uid, format=None):
        inventories = self.get_object(logical_uid)
        serializer = inventoryDetailSerializer(inventories, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class inventoryView(APIView):
    def get(self, request):
        inventories = inventory.objects.all()
        serializer = inventorySerializer(inventories, many=True)
        return Response({"Inventory" : serializer.data})

    def post(self, request, format=None):
        inventories = request.data.get('Inventory')
        serializer = inventorySerializer(data=inventories)
        if serializer.is_valid(raise_exception=True):
            inventory_saved = serializer.save()
        return Response({"success": "Item '{}' created successfully".format(inventory_saved.name)})

    def put(self, request, logical_uid):
        saved_inventory = get_object_or_404(inventory.objects.all(), pk=logical_uid)
        data = request.data.get('inventory')
        serializer = inventorySerializer(instance=saved_inventory, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            inventory_saved = serializer.save()
        return Response({"success": "{}'s quantity updated successfully to {}".format(inventory_saved.logical_uid, inventory_saved.qty)})

    def delete(self, request, deleted_logical_uid):
        inventories = get_object_or_404(inventory.objects.all(), pk = deleted_logical_uid)
        inventories.delete()
        return Response({"message": "Item with logical_uid `{}` has been deleted.".format(deleted_logical_uid)},status=204)

class loggingView(APIView):
    def get(self, request):
        loggings = logging.objects.all()
        serializer = loggingSerializerGet(loggings, many=True)
        return Response({"logging": serializer.data})
    
    def post(self, request):
        loggings = request.data.get('logging')
        serializer = loggingSerializer(data=loggings)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            logging_saved = serializer.save()
        return Response({"success": "Logging for {} created successfully".format(logging_saved.logical_uid)})

    def put(self, request, update_id):
        saved_inventory = get_object_or_404(logging.objects.all(), pk=update_id)
        data = request.data.get('logging')
        serializer = loggingSerializer(instance=saved_inventory, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            logging_saved = serializer.save()
        return Response({"success": "{}'s log updated".format(logging_saved.id)})

    def delete(self, request, delete_id):
        loggings = get_object_or_404(logging.objects.all(), pk = delete_id)
        loggings.delete()
        return Response({"message": "Log with id `{}` has been deleted.".format(delete_id)},status=204)