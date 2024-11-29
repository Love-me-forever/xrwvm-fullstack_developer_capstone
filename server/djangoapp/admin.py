from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 3

class CarAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']
    inlines = [CarModelInline]

admin.site.register(CarMake, CarMakeAdmin)

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ['car_make', 'type', 'year']
    search_fields = ['name', 'car_make__name']


admin.site.register(CarModel, CarModelAdmin)


