from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (HomeView, 
                    RoomView, 
                    BookingCreateView,
                    BookingDeleteView)

from .views_rest import RoomViewSet, BookingViewSet

router = DefaultRouter()
router.register('room', RoomViewSet, basename='rooms')
router.register('booking', BookingViewSet, basename='booking')

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug>/', RoomView.as_view(), name='room'),
    path('<slug>/book/', BookingCreateView.as_view(), name='book'),
    path('<pk>/cancel/', BookingDeleteView.as_view(), name='bookcancel'),

    path('api/v1/', include(router.urls)),
]