from django.contrib import admin

# Register your models here.
from .models import Cafe, Review, Employee, Customer, Menu, Order, OrderItem, Payment, Offer

admin.site.register(Cafe)
admin.site.register(Review)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Offer)