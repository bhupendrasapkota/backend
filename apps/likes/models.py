from django.db import models

class Likes(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    photo = models.ForeignKey('Photos', models.DO_NOTHING)
    liked_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'likes'
        unique_together = (('user', 'photo'),)