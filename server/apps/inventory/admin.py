from django.contrib import admin

from .models import Company, LaundryItem, Location, LocationLaundryItem, Bag

admin.site.register(Company)
admin.site.register(LaundryItem)
admin.site.register(Bag)

class LocationLaundryInline(admin.TabularInline):
    model = LocationLaundryItem
    extra = 0

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    # Change List
    list_display = ["name",]

    # Change Form
    inlines = [LocationLaundryInline]