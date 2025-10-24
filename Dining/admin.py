from django.contrib import admin
from .models import DiningTable,Customer
# Register your models here.
class Adminmodel(admin.ModelAdmin):
    pass

admin.site.register(DiningTable,Adminmodel)
admin.site.register(Customer,Adminmodel)