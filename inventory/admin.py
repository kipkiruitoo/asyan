from django.contrib import admin
from .models import Category, Products, Pallet, Warehouse

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Pallet)
admin.site.register(Warehouse)
# Register your models here.
