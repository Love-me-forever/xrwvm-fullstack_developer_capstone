from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 3

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']
    inlines = [CarModelInline]

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ['car_make', 'type', 'year']
    search_fields = ['name', 'car_make__name']

# Registering models with their respective admins
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)


