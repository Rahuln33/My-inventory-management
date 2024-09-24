from rest_framework import generics, status
from rest_framework.response import Response
from django.core.cache import cache
from .models import Item
from .serializers import ItemSerializer

class ItemCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        cached_item = cache.get(f'item_{item_id}')
        
        if cached_item:
            return Response(cached_item)

        try:
            instance = self.get_object()
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        cache.set(f'item_{item_id}', serializer.data)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        try:
            instance = self.get_object()
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            cache.set(f'item_{item_id}', serializer.data)  # Update cache
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        try:
            instance = self.get_object()
            instance.delete()
            cache.delete(f'item_{item_id}')  # Remove from cache
            return Response({'message': 'Item deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
