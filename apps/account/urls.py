from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UpdateRoleView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('update-role/<int:pk>/', UpdateRoleView.as_view(), name='update-role')
]