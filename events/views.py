from django.shortcuts import render
from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Event
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import EventSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class EventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
        'description',
    ]

    ordering_fields = [
        'comments_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
