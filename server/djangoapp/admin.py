from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 4

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']

# Register CarModel with CarModelAdmin
admin.site.register(CarModel, CarModelAdmin)

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['type', 'date']
    inlines = [CarModelInline]

# Register CarMake with CarMakeAdmin
admin.site.register(CarMake, CarMakeAdmin)

