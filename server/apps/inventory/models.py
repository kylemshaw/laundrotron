from django.db import models
from django.core.validators import MinValueValidator


class Company(models.Model):    
    class Categories(models.TextChoices):
        CLEANING_SERVICE = 'cleaning_service', 'Cleaning Service'
        CUSTOMER = 'customer', 'Customer'

    name = models.CharField(max_length=250, blank=False, null=False)
    category = models.CharField(
        max_length=200,
        blank=False, 
        null=False,
        choices=Categories.choices,
        default=Categories.CUSTOMER,
    )
    # address
    # phone
    
    def __str__(self):
       return f"{self.name}"


class LaundryItem(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = "Laundry Item"
        verbose_name_plural = "Laundry Items"

    def __str__(self):
       return f"{self.name}"


class Location(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    laundry = models.ManyToManyField(LaundryItem, through='LocationLaundryItem')
    # address

    def __str__(self):
       return f"{self.name}"


class LocationLaundryItem(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    laundry_item = models.ForeignKey(LaundryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Location Laundry Item"
        verbose_name_plural = "Location Laundry Items"
        

    def __str__(self):
       return f"{self.location.name} {self.laundry_item.name} ({self.quantity})"


class Bag(models.Model):    
       
    class State(models.TextChoices):
        EMPTY = 'empty', 'Empty'
        CLEAN = 'clean', 'Clean'
        DIRTY = 'dirty', 'Dirty'
    
    class Categories(models.TextChoices):
        CHIPMUNK = 'chipmunk', 'Chipmunk'

    barcode = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(
        max_length=200,
        blank=False, 
        null=False,
        choices=Categories.choices, 
        default=Categories.CHIPMUNK
    )
    state = models.CharField(max_length=200, choices=State.choices, default=State.EMPTY)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)

    def __str__(self):
       return f"Bag #{self.barcode}"