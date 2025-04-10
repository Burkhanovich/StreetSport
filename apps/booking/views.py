from django.utils import timezone
from datetime import timedelta

from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Booking
from .serializers import BookingSerializer
from apps.account.permissions import IsUser
from apps.stadium.models import Stadium
from drf_spectacular.utils import extend_schema


@extend_schema(
    request=BookingSerializer,
    responses={201: BookingSerializer}
)
class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsUser]

@extend_schema(
    responses={200: BookingSerializer(many=True)}
)
class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 1:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)


@extend_schema(
    responses={200: BookingSerializer(many=True)}
)
class StadiumBookingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            stadium = Stadium.objects.get(pk=pk)
        except Stadium.DoesNotExist:
            return Response({"error": "Stadion topilmadi"}, status=404)

        bookings = stadium.bookings.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

@extend_schema(
    responses={200: serializers.ListSerializer(child=serializers.DictField())}
)
class StadiumAvailableSlotsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            stadium = Stadium.objects.get(pk=pk)
        except Stadium.DoesNotExist:
            return Response({"error": "Stadion topilmadi"}, status=404)

        today = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = today + timedelta(days=7)
        working_hours_start = 8
        working_hours_end = 22

        bookings = stadium.bookings.filter(
            start_time__gte=today,
            end_time__lte=end_date
        ).order_by("start_time")

        available_slots = []
        current_date = today

        while current_date < end_date:
            day_start = current_date.replace(hour=working_hours_start)
            day_end = current_date.replace(hour=working_hours_end)

            day_bookings = bookings.filter(
                start_time__date=current_date.date()
            )

            if not day_bookings:
                available_slots.append({
                    "start_time": day_start.isoformat(),
                    "end_time": day_end.isoformat()
                })
            else:
                current_time = day_start
                for booking in day_bookings:
                    if current_time < booking.start_time:
                        available_slots.append({
                            "start_time": current_time.isoformat(),
                            "end_time": booking.start_time.isoformat()
                        })
                    current_time = max(current_time, booking.end_time)

                if current_time < day_end:
                    available_slots.append({
                        "start_time": current_time.isoformat(),
                        "end_time": day_end.isoformat()
                    })

            current_date += timedelta(days=1)

        return Response(available_slots)





