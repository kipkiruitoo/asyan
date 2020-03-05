from django.db import models
from accounts.models import User
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
    


    reoder_level = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    pallet = models.ForeignKey(Pallet, related_name='products', on_delete=models.CASCADE)
    item_description = models.TextField( default='')
    def __str__(self):
        return self.name
        




class Batch(models.Model):
    STATE_CHOICES = (
    ('Finished', 'Finished'),
    ('Current', 'Current'),
    ('Later', 'Later'),)

    date_delivery = models.DateField(auto_now_add=True)
    date_expiry = models.DateField()
    date_finished = models.DateField()
    delivered_quantity = models.IntegerField()
    quantity_remaining = models.IntegerField()
    pallet = models.ForeignKey(Pallet, related_name='batch', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='batch', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='batch', on_delete=models.CASCADE)
    supplier = models.ForeignKey('supplier.Company', related_name='batch', on_delete=models.CASCADE)
    state = models.CharField(max_length=20, default='Later', choices=STATE_CHOICES)
    def BatchNO(self):
        return str(self.pk) + '/' + str(self.supplier.user)+ '/' +str(self.receiver) 

    def __str__(self):
        batchno = self.BatchNO()
        return batchno

class Transaction(models.Model):
    product = models.ForeignKey(Products, related_name='transaction', on_delete=(models.CASCADE))
    date = models.DateField(auto_now_add=True)
    batch = models.ForeignKey(Batch, related_name='transaction', on_delete=(models.CASCADE))
    quantity = models.PositiveIntegerField()
    sold_by = models.ForeignKey(User, related_name='transaction', on_delete=(models.CASCADE))
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.pk