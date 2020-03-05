from .forms import ProductsForm, CategoryForm, WarehouseForm, PalletForm, BatchForm, TransactionForm
from .models import Products, Warehouse, Category, Pallet, Batch, Transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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

class BatchCreateView(LoginRequiredMixin, CreateView):
    model = Batch
    form_class = BatchForm
    success_url = reverse_lazy('inventory:batch_list')


class BatchListView(LoginRequiredMixin, ListView):
    model = Batch


def transaction_create_view(request):
    template = 'inventory/transaction_form.html'
    if request.method == 'POST':
        form = TransactionForm
        if form.is_valid():
            #create transaction
            transaction = form.save(commit=False)
            
            #alter product
            product = Products.objects.get(id=transaction.product)
            product.quantity_available = product.quantity_available - transaction.quantity

            # alter batch
            batches = Batch.objects.filter(state='Current')
            if lens(batches) == 1:
                batch = batches[0]
                if batch.quantity_remaining > transaction.quantity:
                    batch.quantity_remaining = batch.quantity_remaining - transaction.quantity



class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction                    