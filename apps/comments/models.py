from django.db import models

class Comments(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey('users.User', models.DO_NOTHING)
    photo = models.ForeignKey('photos.Photos', models.DO_NOTHING)
    comment_text = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'