from django.contrib import admin
from .models import MenuItem, Booking


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image_url')
    search_fields = ('name',)
    list_filter = ('price',)
    fields = ('name', 'price', 'description', 'image_url')


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Booking)
