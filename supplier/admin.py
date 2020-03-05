from django.contrib import admin

# Register your models here.
from supplier.models import Tender,Company

admin.site.register(Tender)
admin.site.register(Company)