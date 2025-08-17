from django.contrib import admin
from . import models
# Register your models here. u:admin p:1234
# Test user u:testuser p:pass4testuser

admin.site.register(models.Vendor)
admin.site.register(models.Product)
admin.site.register(models.ProductCategory)