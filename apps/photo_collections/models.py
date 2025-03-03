from django.db import models

class PhotoCollections(models.Model):
    photo = models.OneToOneField('photos.Photos', models.DO_NOTHING, primary_key=True)  # The composite primary key (photo_id, collection_id) found, that is not supported. The first column is selected.
    collection = models.ForeignKey('collection.Collections', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'photo_collections'
        unique_together = (('photo', 'collection'),)