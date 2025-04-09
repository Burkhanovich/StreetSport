from apps.account.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import StadiumSerializer, StadiumViewSerializer
from .models import Stadium
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes


@extend_schema(
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
                "owner": {"type": "integer"},  # Admin uchun ko‘rinadi
                "manager": {"type": "integer", "nullable": True},
                "images": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "format": "binary"
                    }
                }
            },
            "required": ["location", "owner"]  # Admin uchun owner majburiy
        }
    },
    responses={201: StadiumSerializer}
)
class CreateStadiumView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = StadiumSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save()  # owner qo‘lda kiritilmaydi, serializer’da boshqariladi



class StadiumListView(generics.ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumViewSerializer

class StadiumDetailView(generics.RetrieveAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumViewSerializer


