from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import user, inventory, logging
from .serializers import userSerializer, inventorySerializer, inventoryQtySerializer, loggingSerializer, inventoryDetailSerializer

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
            raise Http404

    def get(self, request, detailed_uid, format=None):
        snippet = self.get_object(detailed_uid)
        serializer = inventoryDetailSerializer(snippet)
        return Response(serializer.data)

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

    def put(self, request, logical_uid):
        saved_inventory = get_object_or_404(inventory.objects.all(), pk=logical_uid)
        data = request.data.get('inventory')
        serializer = inventorySerializer(instance=saved_inventory, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            inventory_saved = serializer.save()
        return Response({"success": "UID {}'s name updated successfully to {}".format(inventory_saved.logical_uid, inventory_saved.name)})

class loggingView(APIView):
    def get(self, request):
        loggings = logging.objects.all()
        serializer = loggingSerializer(loggings, many=True)
        return Response({"logging": serializer.data})
    
    def post(self, request):
        loggings = request.data.get('logging')
        serializer = loggingSerializer(data=loggings)
        if serializer.is_valid(raise_exception=True):
            logging_saved = serializer.save()
        return Response({"success": "Logging '{}' created successfully".format(logging_saved.logical_uid)})
