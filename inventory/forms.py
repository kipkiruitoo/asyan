from django.forms import ModelForm, TextInput, NumberInput
from .models import Products, Category, Warehouse, Pallet

class ProductsForm(ModelForm):

    class Meta():
        model = Products
        fields = '__all__'
        # widgets = {
        #     'name': TextInput(attrs={'placeholder': "John Doe", "class": "form-control"}),
        #     'selling_price': NumberInput(attrs={"class": "form-control"}),

        #     'cost_price': NumberInput(attrs={"class": "form-control"}),

        #     'quantity': NumberInput(attrs={"class": "form-control"}),

        #     'quantity_available': NumberInput(attrs={"class": "form-control"}),
        #     'unit_measure': TextInput(attrs={"class": "form-control"}),

        #     'reoder_level': NumberInput(attrs={"class": "form-control"}),
        #     'category': TextInput(attrs={"class": "form-control"}),

        #     'pallet': TextInput(attrs={"class": "form-control"}),



        # }   



        

class CategoryForm(ModelForm):

    class Meta():
        model = Category
        fields = '__all__'
        
class WarehouseForm(ModelForm):

    class Meta():
        model = Warehouse
        fields = '__all__'
        
        
class PalletForm(ModelForm):

    class Meta():
        model = Pallet
        fields = '__all__'