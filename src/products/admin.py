from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # all these, coming from model
    list_display = ['__str__', 'description', 'price']
    # creates a search field based on description
    # if we want more search options, just add in the field
    # i.e. search_fields = ['description', 'price']
    search_fields = ['description']
    # list filter is the filter in the right box
    list_filter = ['price']
    # list editable allow us to make changes on the object list
    list_editable = ['price']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
