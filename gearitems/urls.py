from django.urls import path
from gearitems import views

urlpatterns = [
    path('gearitems/', views.GearItemList.as_view()),
    path('gearitems/<int:pk>/', views.GearItemDetail.as_view())
]
