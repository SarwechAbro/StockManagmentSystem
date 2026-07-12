from django.contrib import admin

from .models import Item, category, section, StockIn, StockOut

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'quantity']
    search_fields = ['name']
    list_filter = ['name']
    ordering = ['id']



@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']
    ordering = ['id']


@admin.register(section)
class sectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']
    ordering = ['id']  

@admin.register(StockIn)
class stockAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity', 'date_of_entry','category', 'reciever']
    search_fields = ['item']
    list_filter = ['date_of_entry']
    ordering = ['id']    


@admin.register(StockOut)
class stock_outAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity', 'date_of_issue','category', 'emp_name']
    search_fields = ['item']
    list_filter = ['date_of_issue']
    ordering = ['id']      