from django.db import models

# Create your models here.
from django.utils import timezone

from accounts.models import User
from inventory.models import Products


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_admin')
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    registered_on = models.DateField(auto_now_add=True)


class Tender(models.Model):
    title = models.CharField(max_length=100, default='')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='tender_product')
    quantity = models.PositiveIntegerField(default=0)
    opened_on = models.DateField(auto_now_add=True)
    application_deadline = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    rating = models.PositiveIntegerField(default=1)
    requirements = models.TextField()


class TenderApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applicant')
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE, related_name='tender', default=1)
    application_date = models.DateField(auto_now_add=True)
    is_successful = models.BooleanField(default=False)
    discount_terms = models.TextField()

