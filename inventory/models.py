from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=256)
    
class Warehouse(models.Model):
    name = models.CharField(unique=True, max_length=50)
    location = models.CharField(unique=True, max_length=50)
    address =  models.CharField(unique=True, max_length=50)
    


class Products(models.Model):
    name = models.CharField(max_length=255, unique=True)
    selling_price = models.PositiveIntegerField()	
    cost_price = models.PositiveIntegerField()	
    quantity = models.PositiveIntegerField()
    reoder_level = models.PositiveIntegerField()	
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('products:product_detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']
        
        
class Pallet(models.Model):
    name = models.CharField(max_length=50)
    warehouse = models.ForeignKey(Warehouse, related_name='pallet', on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, )
    description = models.CharField(max_length=250, null=True)
    
    class Meta:
        unique_together = ('name', 'warehouse')


