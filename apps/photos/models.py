from django.db import models

class Photos(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    image_url = models.TextField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    width = models.IntegerField()
    height = models.IntegerField()
    size_in_bytes = models.BigIntegerField()
    format = models.TextField()  # This field type is a guess.
    ai_tags = models.JSONField(blank=True, null=True)
    is_approved = models.BooleanField(blank=True, null=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    likes_count = models.IntegerField(blank=True, null=True)
    comments_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photos'