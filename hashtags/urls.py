from django.urls import path, include
from . import views

urlpatterns = [
    path('cloth/', views.ClothListView.as_view(), name='cloth'),
    path('kinder_cloth/', views.KinderClothListView.as_view(), name='kinder_cloth'),
    path('young_cloth/', views.YoungClothListView.as_view(), name='young_cloth'),
    path('old_cloth/', views.OldClothListView.as_view(), name='old_cloth'),
]