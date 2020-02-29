from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
class Warehouse(models.Model):
    name = models.CharField(unique=True, max_length=50)
    location = models.CharField(max_length=50)
    address =  models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Pallet(models.Model):
    name = models.CharField(max_length=50)
    warehouse = models.ForeignKey(Warehouse, related_name='pallet', on_delete=models.CASCADE)
    description = models.CharField(max_length=250, null=True)
    
    class Meta:
        unique_together = ('name', 'warehouse')
        
    def __str__(self):
        return self.name
        
        
class Products(models.Model):

    UNIT_CHOICES = (
        ('Kilograms', 'Kilograms'),
        ('Liters', 'Liters'),
        ('Meters', 'Meters'),
        ('Piece', 'Piece'),
        ('Tonne', 'Tonne'),


    )
    VED_TYPE = (
        ('Vital', 'Vital'),
        ('Essential', 'Essential'),
        ('Desirable', 'Desirable'),



    )
    INVENTORY_TYPE = (
        ('Vital', 'Vital'),
        ('Essential', 'Essential'),
        ('Desirable', 'Desirable'),

    )
    MB_TYPE= (
        ('make', 'Make'),
        ('buy', 'Buy'),


    )
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    pallet = models.ForeignKey(Pallet, related_name='products', on_delete=models.CASCADE)

    VED_analysis = unit_measure = models.CharField(max_length=20, null=False,default='', choices=VED_TYPE)
    buy_or_make=unit_measure = models.CharField(max_length=20, null=False,default='', choices=MB_TYPE)
    selling_price = models.PositiveIntegerField(null=True)
    cost_price = models.PositiveIntegerField(null=True)
    selling_price = models.PositiveIntegerField()
    cost_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    quantity_available = models.PositiveIntegerField(null=True)
    unit_measure = models.CharField(max_length=20, null=False, choices=UNIT_CHOICES)
    ABC_category= models.CharField(max_length=2,null=True)
    FSN_analysis= models.CharField(max_length=255,null=True)
    reoder_level = models.PositiveIntegerField(default='')
    safety_stock_level = models.PositiveIntegerField(default=0)
    item_description = models.CharField(max_length=255, default='')


    reoder_level = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    pallet = models.ForeignKey(Pallet, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        



