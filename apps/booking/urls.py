from django.urls import path
from .views import (
    BookingListView,
    BookingCreateView,
    StadiumAvailableSlotsView,
    StadiumBookingsView,

)

urlpatterns = [
    path('list/', BookingListView.as_view(), name='booking-list'),
    path('create/', BookingCreateView.as_view(), name='create_booking'),
    path('stadium-bookings/<int:pk>/', StadiumBookingsView.as_view(), name='stadium_bookings'),
    path('available-slots/<int:pk>/', StadiumAvailableSlotsView.as_view(), name='stadium-available-slots'),
]


