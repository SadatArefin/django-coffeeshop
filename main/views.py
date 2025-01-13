from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Cafe, Review, Employee, Customer, Menu, Order, OrderItem, Payment, Offer
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import OrderForm, OrderItemForm

class CafeListView(ListView):
    model = Cafe
    template_name = 'main/cafe_list.html'

class CafeDetailView(DetailView):
    model = Cafe
    template_name = 'main/cafe_detail.html'


def OrderCreateView(request):
    if request.method == 'GET':
        order_form = OrderForm()
        order_item_form = OrderItemForm()
        return render(request, 'main/create_order.html', {
            'order_form': order_form,
            'order_item_form': order_item_form
        })
    elif request.method == 'POST':
        order_form = OrderForm(request.POST)
        order_item_form = OrderItemForm(request.POST)
        if order_form.is_valid() and order_item_form.is_valid():
            order = order_form.save()
            order_item = order_item_form.save(commit=False)
            order_item.order = order
            order_item.save()
            return redirect('main:order-list')
        return render(request, 'main/create_order.html', {
            'order_form': order_form,
            'order_item_form': order_item_form
        })

# def get_menu_items(request, cafe_id):
#     menu_items = Menu.objects.filter(cafe_id=cafe_id)
#     menu_items_data = [{'id': item.id, 'name': item.name, 'price': item.price} for item in menu_items]
#     return JsonResponse(menu_items_data, safe=False)

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review_detail.html'

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'

class MenuListView(ListView):
    model = Menu
    template_name = 'menu_list.html'

class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu_detail.html'



class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'orderitem_list.html'

class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'orderitem_detail.html'

class PaymentListView(ListView):
    model = Payment
    template_name = 'payment_list.html'

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment_detail.html'

class OfferListView(ListView):
    model = Offer
    template_name = 'offer_list.html'

class OfferDetailView(DetailView):
    model = Offer
    template_name = 'offer_detail.html'