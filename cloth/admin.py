# cloth/admin.py
from django.contrib import admin
from .models import Product, Order, Customer, Tag

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Tag)
