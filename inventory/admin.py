from django.contrib import admin
from .models import Category, Products, Pallet, Warehouse, Batch

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Pallet)
admin.site.register(Warehouse)
admin.site.register(Batch)

# Register your models here.
