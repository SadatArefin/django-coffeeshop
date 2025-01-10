from django.db import models

class Cafe(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=12)
    website = models.URLField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cafe.name + " Review"
    
class Employee(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    position = models.CharField(max_length=100)
    date_hired = models.DateTimeField(auto_now_add=True)
    date_fired = models.DateTimeField(null=True, blank=True)
    access_level = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Customer(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
class Menu(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    date_fulfilled = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.customer.full_name + " Order"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_item.name + " Order Item"
    
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.customer.full_name + " Payment"

class Offer(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name