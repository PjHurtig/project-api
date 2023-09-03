from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    BIKE = 'bike'
    CLIMBING = 'climbing'
    HIKING = 'hiking'
    OTHER = 'other'

    GEAR_LIST_CATEGORIES = [
        (BIKE, 'Bike'),
        (CLIMBING, 'Climbing'),
        (HIKING, 'Hiking'),
        (OTHER, 'Other'),
    ]

    category = models.CharField(
        max_length=20, choices=GEAR_LIST_CATEGORIES, default=OTHER)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    image = models.ImageField(
        upload_to='images/', default='../default_post_wu5uso', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
