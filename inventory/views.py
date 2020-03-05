from .forms import ProductsForm, CategoryForm, WarehouseForm, PalletForm
from .models import Products, Warehouse, Category, Pallet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False
##############################################################################
# Products views


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Products
    form_class = ProductsForm
    success_url = reverse_lazy('inventory:products_list')


class ProductsDetailView(LoginRequiredMixin, DetailView):
    model = Products


class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    form_class = ProductsForm
    template_name_suffix = '_update_form'


class ProductsDeleteView(LoginRequiredMixin, DeleteView):
    model = Products
    success_url = reverse_lazy('management:employee_list')


class ProductsListView(LoginRequiredMixin, ListView):
    model = Products
    template_name = 'inventory/products_list.html'
    products = Products.objects.all()
    context = locals()
    # context['products'] = products

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'products': self.products})

    # print(products)

#######################################################################################

##############################################################################
# Category views


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('inventory:category_list')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name_suffix = '_update_form'


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('management:employee_list')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

#######################################################################################

##############################################################################
# Warehouse views


class WarehouseCreateView(LoginRequiredMixin, CreateView):
    model = Warehouse
    form_class = WarehouseForm
    success_url = reverse_lazy('inventory:warehouse_list')


class WarehouseDetailView(LoginRequiredMixin, DetailView):
    model = Warehouse


class WarehouseUpdateView(LoginRequiredMixin, UpdateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name_suffix = '_update_form'


class WarehouseDeleteView(LoginRequiredMixin, DeleteView):
    model = Warehouse
    success_url = reverse_lazy('management:employee_list')


class WarehouseListView(LoginRequiredMixin, ListView):
    model = Warehouse

#######################################################################################

##############################################################################
# Pallet views


class PalletCreateView(LoginRequiredMixin, CreateView):
    model = Pallet
    form_class = PalletForm
    success_url = reverse_lazy('inventory:pallet_list')


class PalletDetailView(LoginRequiredMixin, DetailView):
    model = Pallet


class PalletUpdateView(LoginRequiredMixin, UpdateView):
    model = Pallet
    form_class = PalletForm
    template_name_suffix = '_update_form'


class PalletDeleteView(LoginRequiredMixin, DeleteView):
    model = Pallet
    success_url = reverse_lazy('management:employee_list')


class PalletListView(LoginRequiredMixin, ListView):
    model = Pallet

#######################################################################################
