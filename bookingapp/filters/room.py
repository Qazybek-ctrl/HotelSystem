from django_filters import rest_framework as filters

from .fields import IntegerInFilter
from ..models import Room, Booking

class RoomFilterSet(filters.FilterSet):
    name = filters.BaseInFilter()
    price = filters.BaseInFilter()
    seat = IntegerInFilter()

    class Meta:
        model = Room
        fields = ('name', 'price', 'seat')

class BookingFilterSet(filters.FilterSet):
    user = filters.BaseInFilter()
    room = filters.BaseInFilter()
    start_day = filters.DateFilter()
    end_day = filters.DateFilter()

    class Meta:
        model = Booking
        fields = ('user', 'room', 'start_day', 'end_day')
