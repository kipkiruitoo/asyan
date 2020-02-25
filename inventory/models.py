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

    )
    name = models.CharField(max_length=255, unique=True)
    selling_price = models.PositiveIntegerField()	
    cost_price = models.PositiveIntegerField()	
    quantity = models.PositiveIntegerField()
    quantity_available = models.PositiveIntegerField(null=True)
    unit_measure = models.CharField(max_length=20, null=False, choices=UNIT_CHOICES)

    reoder_level = models.PositiveIntegerField()	
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    pallet = models.ForeignKey(Pallet, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('products:product_detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']
        
        



