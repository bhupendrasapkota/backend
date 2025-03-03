from rest_framework import serializers
from apps.users.models import User
from apps.authentication.authentication import generate_jwt_tokens
from apps.authentication.services import create_user
import re
from django.contrib.auth.hashers import check_password

class UserRegistrationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    password = serializers.CharField(write_only=True, min_length=8)
    role = serializers.CharField(default='user', required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

    def validate_password(self, value):
        """Enforce strong password policy"""
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'\d', value):
            raise serializers.ValidationError("Password must contain at least one digit.")
        if not re.search(r'[@$!%*?&]', value):
            raise serializers.ValidationError("Password must contain at least one special character (@$!%*?&).")
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def create(self, validated_data):
        if "role" not in validated_data:
            validated_data["role"] = "user"
        return create_user(validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from apps.authentication.authentication import generate_jwt_tokens
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        if not user.password or not check_password(data['password'],user.password):
            raise serializers.ValidationError("Invalid credentials")

        return {
            'user_id': user.id,
            'username': user.username,
            'role': user.role,
            'tokens': generate_jwt_tokens(user)
        }
