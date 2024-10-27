from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 4

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']

admin.site.register(CarModel)

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['type', 'date']
    inlines = [CarModelInline]
    
admin.site.register(CarMake)
# Register models here
