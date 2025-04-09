from apps.account.permissions import IsAdminOrOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from .permissions import IsAdminOrStadiumOwner
from .serializers import StadiumSerializer, StadiumViewSerializer
from .models import Stadium
from drf_spectacular.utils import extend_schema


@extend_schema(
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
                "owner": {"type": "integer"},
                "manager": {"type": "integer", "nullable": True},
                "images": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "format": "binary"
                    }
                }
            },
            "required": ["location", "owner"]
        }
    },
    responses={201: StadiumSerializer}
)
class CreateStadiumView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrOwner]
    serializer_class = StadiumSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save()


class StadiumListView(generics.ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumViewSerializer


class StadiumDetailView(generics.RetrieveAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumViewSerializer


@extend_schema(
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
                "owner": {"type": "integer"},
                "manager": {"type": "integer", "nullable": True},
                "images": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "format": "binary"
                    }
                }
            },
            "required": ["location"]
        }
    },
    responses={200: StadiumSerializer}
)
class StadiumUpdateView(generics.UpdateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner, IsAdminOrStadiumOwner]
    parser_classes = [MultiPartParser, FormParser]






