from rest_framework import serializers
from .models import Stadium, StadiumImage


class StadiumImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = StadiumImage
        fields = ['id', 'image']
        read_only_fields = ["id"]


class StadiumSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),  # Fayllarni ro‘yxat sifatida qabul qilish
        write_only=True,
        required=False
    )

    class Meta:
        model = Stadium
        fields = ["id", "location", "owner", "manager", "created_date", "images"]
        read_only_fields = ["id", "created_date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")

        # Faqat Owner bo‘lsa owner maydoni ko‘rinmaydi, Admin bo‘lsa ko‘rinadi
        if request and request.user and request.user.role == 2:
            self.fields.pop("owner", None)  # Owner uchun olib tashlanadi
        elif request and request.user and request.user.role == 1:
            self.fields["owner"].read_only = False  # Admin uchun ko‘rinadi va kiritilishi mumkin

    def validate(self, data):
        owner = data.get("owner")
        manager = data.get("manager")
        request = self.context.get("request")

        # Agar Owner bo‘lsa, owner avtomatik o‘zi bo‘ladi
        if request and request.user and request.user.role == 2:
            data["owner"] = request.user
        else:
            # Admin bo‘lsa, owner kiritilishi shart va role=2 bo‘lishi kerak
            if not owner:
                raise serializers.ValidationError({"owner": "Admin must provide an owner."})
            if owner and owner.role != 2:
                raise serializers.ValidationError({"owner": "Only Owner (role=2) can be the stadium owner."})

        if manager and manager.role != 3:
            raise serializers.ValidationError({"manager": "Only Manager (role=3) can be the stadium manager."})
        return data

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])  # Fayllarni ro‘yxat sifatida olamiz
        stadium = Stadium.objects.create(**validated_data)

        for image in images_data:
            StadiumImage.objects.create(stadium=stadium, image=image)

        return stadium


class StadiumViewSerializer(serializers.ModelSerializer):
    images=StadiumImageSerializer(many=True)
    class Meta:
        model = Stadium
        fields = ["id", "location", "owner", "manager", "created_date", "images"]
        read_only_fields = ["id", "created_date"]

