from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.authentication.permissions import IsAdminUser
from apps.authentication.serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.decorators import action
from django.core.cache import cache
from django.utils.timezone import now
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

class AuthenticationViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User registered successfully", "user_id": user.id, "role": user.role},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        email = request.data.get('email')

        attempts = cache.get(f'failed_attempts_{email}', 0)
        if attempts >= 5:
            return Response({"error": "Too many failed login attempts. Try again later."}, status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            cache.set(f'failed_attempts_{email}', 0, timeout=None)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        cache.set(f'failed_attempts_{email}', attempts + 1, timeout=900)
        return Response({"error": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated, IsAdminUser])
    def admin_only(self, request):
        return Response({"message": "Hello Admin!"}, status=200)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
