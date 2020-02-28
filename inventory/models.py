from django.db import models
from django.urls import reverse


import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(null=True, blank=True, max_length=256)
    
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
    description = models.CharField(max_length=250, null=True, blank=True)
    
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

    def get_absolute_url(self):
        return reverse('inventory:products_detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']
        
        
# class Batch(models.Model):
#     return 
    
#     # def increment_batch_number():
#     #     last_booking = Batch.objects.all().order_by('id').last()
#     #     if not last_booking:
#     #         return 'RNH' + str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + '0000'
#     #     booking_id = last_booking.booking_id
#     #     booking_int = int(booking_id[9: 13])
#     #     new_booking_int = booking_int + 1
#     #     new_booking_id = 'RNH' + str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2) + str(new_booking_int).zfill(4)
#     # return new_booking_id