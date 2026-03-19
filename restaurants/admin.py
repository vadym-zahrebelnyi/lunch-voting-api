from django.contrib import admin
from .models import Restaurant, Menu


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "restaurant", "date")
    list_filter = ("date", "restaurant")
    search_fields = ("restaurant__name", "items")
    date_hierarchy = "date"
