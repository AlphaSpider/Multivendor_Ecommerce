from django.contrib import admin
from . import models
# Register your models here. u:admin p:1234
# Test user u:testuser p:pass4testuser
# Customer u: customer1 p: pass4cust

admin.site.register(models.Vendor)
admin.site.register(models.Product)
admin.site.register(models.ProductCategory)

admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderItems)