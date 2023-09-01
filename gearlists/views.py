from rest_framework import generics, permissions
from django.db.models import Count
from .models import GearList
from .serializers import GearListSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class GearListCreateView(generics.ListCreateAPIView):
    queryset = GearList.objects.annotate(
        gearitem_count=Count('gearitem', distinct=True)
    ).order_by('-created_at')
    serializer_class = GearListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GearListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GearList.objects.all()
    serializer_class = GearListSerializer
    permission_classes = [IsOwnerOrReadOnly]
