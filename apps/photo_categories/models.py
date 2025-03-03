from django.db import models

class PhotoCategories(models.Model):
    photo = models.OneToOneField('photos.Photos', models.DO_NOTHING, primary_key=True)  # The composite primary key (photo_id, category_id) found, that is not supported. The first column is selected.
    category = models.ForeignKey('categories.Categories', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'photo_categories'
        unique_together = (('photo', 'category'),)