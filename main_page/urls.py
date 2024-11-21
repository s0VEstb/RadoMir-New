from django.urls import path
from . import views


urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
    path('about_my_pets/', views.about_my_pets, name='about_my_pets'),
    path('time/', views.time, name='time'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]