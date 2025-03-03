from django.db import models

class Downloads(models.Model):
    user = models.ForeignKey('users.User', models.DO_NOTHING)
    photo = models.ForeignKey('photos.Photos', models.DO_NOTHING)
    downloaded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downloads'