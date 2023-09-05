from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from drf_api.permissions import IsOwnerOrReadOnly
from .models import GearItem
from .serializers import GearItemSerializer, GearItemDetailSerializer


class GearItemList(generics.ListCreateAPIView):
    """
    List GearItem or create a GearItem if logged in.
    """
    serializer_class = GearItemSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
    queryset = GearItem.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gearlist']

    def perform_create(self, serializer):
        gearlist = serializer.validated_data.get('gearlist')

        if gearlist.owner != self.request.user:
            raise PermissionDenied(
                "You do not own this list!")
        serializer.save(owner=self.request.user)


class GearItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a GearItem, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GearItemDetailSerializer
    queryset = GearItem.objects.all()
