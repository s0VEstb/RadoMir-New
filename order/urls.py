from django.urls import path, include
from . import views


urlpatterns = [
    path('order_create/', views.OrderListView.as_view(), name='order_create'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/<int:id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:id>/update/', views.UpdateOrderView.as_view(), name='order_update'),
    path('orders/<int:id>/delete/', views.DeleteOrderView.as_view(), name='order_delete'),
    path('create_order/', views.CreateOrderView.as_view(), name='create_order'),
]