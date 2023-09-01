from django.urls import path
from . import views

urlpatterns = [
    path('gearlists/', views.GearListCreateView.as_view()),
    path('gearlists/<int:pk>/', views.GearListDetailView.as_view()),
]
