from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UpdateRoleView, CreateManager, CreateOwner

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('update-role/<int:pk>/', UpdateRoleView.as_view(), name='update-role'),
    path('add-manager/', CreateManager.as_view(), name='add-manager'),
    path('add-owner/', CreateOwner.as_view(), name='add-owner'),
]