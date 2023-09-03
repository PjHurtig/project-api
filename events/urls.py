from django.urls import path
from events import views

urlpatterns = [
    path('events/', views.EventView.as_view()),
    path('events/<int:pk>/', views.EventDetailView.as_view())
]
