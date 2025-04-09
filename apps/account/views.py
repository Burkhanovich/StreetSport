from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer,UpdateRoleSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .permissions import IsOwner, IsAdmin, IsManager
from django.shortcuts import get_object_or_404
from .models import Account
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UpdateRoleView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = UpdateRoleSerializer

    def patch(self, request, pk):
        user = get_object_or_404(Account, id=pk)
        role = request.data.get('role')
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if role not in [1, 2, 3, 4]:
            return Response({"detail": "Wrong role."}, status=status.HTTP_400_BAD_REQUEST)

        if request.user.role == 1:
            if user.id == request.user.id:
                return Response({"detail": "O'z rolingizni o'zgartira olmaysiz"}, status=400)
            user.role = role
            user.save()
            return Response({"detail": 'The role has been changed.'})


        if request.user.role == 2:
            if user.role == 1 or user.role==2:
                return Response({"detail": "You do not have such permission."}, status=status.HTTP_400_BAD_REQUEST)
            if role == 2 or role == 1:
                    return Response({"detail": "You do not have such permission."}, status=status.HTTP_400_BAD_REQUEST)
            user.role = role
            user.save()
            return Response({"detail": "The role has been changed."})

        return Response({"detail": "You do not have such permission."}, status=status.HTTP_403_FORBIDDEN)

