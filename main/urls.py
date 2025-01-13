from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('cafes/', views.CafeListView.as_view(), name='cafe-list'),
    path('cafes/<int:pk>/', views.CafeDetailView.as_view(), name='cafe-detail'),
    path('cafes/create-order/', views.OrderCreateView, name='create-order'),
    # path('cafes/<int:cafe_id>/menu-items/', views.OrderCreateView.get_menu_items, name='get-menu-items'),
    path('orders/', views.OrderListView.as_view(), name='order-list'),

    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('menus/', views.MenuListView.as_view(), name='menu-list'),
    path('menus/<int:pk>/', views.MenuDetailView.as_view(), name='menu-detail'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order-items/', views.OrderItemListView.as_view(), name='orderitem-list'),
    path('order-items/<int:pk>/', views.OrderItemDetailView.as_view(), name='orderitem-detail'),
    path('payments/', views.PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment-detail'),
    path('offers/', views.OfferListView.as_view(), name='offer-list'),
    path('offers/<int:pk>/', views.OfferDetailView.as_view(), name='offer-detail'),
]