from django.db import models

class Categories(models.Model):
    name = models.CharField(unique=True, max_length=100)
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'categories'