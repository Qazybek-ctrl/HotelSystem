from django.contrib import admin

from .models import Room, Booking

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seat')
    list_display_links = ('name', 'price')
    search_fields = ('name', 'price')
    list_filter = ('price', 'seat')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'start_day', 'end_day')
    list_editable = ('start_day', 'end_day')
    search_fields = ('user', 'room')

admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)