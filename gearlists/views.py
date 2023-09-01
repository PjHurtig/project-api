from rest_framework import generics, permissions
from .models import GearList
from .serializers import GearListSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class GearListCreateView(generics.ListCreateAPIView):
    queryset = GearList.objects.all()
    serializer_class = GearListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GearListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GearList.objects.all()
    serializer_class = GearListSerializer
    permission_classes = [IsOwnerOrReadOnly]
