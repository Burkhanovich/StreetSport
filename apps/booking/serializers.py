from rest_framework import serializers
from .models import Booking, Stadium, Account

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "stadium", "user", "start_time", "end_time", "created_date"]
        read_only_fields = ["id", "user", "created_date"]

    def validate(self, data):
        request = self.context.get("request")
        if request and request.user:
            data["user"] = request.user

        stadium = data.get("stadium")
        user = data.get("user")

        if user.role != 4:
            raise serializers.ValidationError({"user": "Faqat User (role=4) stadionni bron qilishi mumkin."})

        return data