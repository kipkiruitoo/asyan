from django.contrib import admin
from .models import Category, Products, Pallet, Warehouse, Batch, Transaction

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Pallet)
admin.site.register(Warehouse)
admin.site.register(Batch)
admin.site.register(Transaction)


# Register your models here.
