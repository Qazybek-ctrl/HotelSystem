from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .filters.room import RoomFilterSet, BookingFilterSet
from .serializers.serializers import RoomSerializer, BookingSerializer

from django_filters.rest_framework import DjangoFilterBackend

from .models import Room,Booking

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookingFilterSet

    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoomFilterSet

    serializer_class = RoomSerializer
    queryset = Room.objects.all()