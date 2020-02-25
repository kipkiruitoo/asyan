from django import forms
from .models import Products, Category, Warehouse, Pallet

class ProductsForm(forms.ModelForm, forms.MultiWidget):

    class Meta():
        model = Products
        fields = '__all__'
        exclude = ['quantity_available']      



        

class CategoryForm(forms.ModelForm):

    class Meta():
        model = Category
        fields = '__all__'
        
class WarehouseForm(forms.ModelForm):

    class Meta():
        model = Warehouse
        fields = '__all__'
        
        
class PalletForm(forms.ModelForm):

    class Meta():
        model = Pallet
        fields = '__all__'