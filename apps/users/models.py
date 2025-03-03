from django.db import models
import uuid

class User(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    password = models.TextField()
    full_name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True, choices=ROLE_CHOICES, default='user')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    about = models.TextField(blank=True, null=True)
    contact = models.JSONField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'users'
    
    def __str__(self):
        return self.username