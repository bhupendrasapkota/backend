from django.db import transaction
from django.contrib.auth.hashers import make_password
from apps.users.models import User

def create_user(validated_data):
    """Create a new user securely."""
    with transaction.atomic():
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)
