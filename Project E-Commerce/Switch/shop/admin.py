from django.contrib import admin

# Register your models here.
from .models import Product, Order
from .models import Category, Contact
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Order)
