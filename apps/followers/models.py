from django.db import models

class Followers(models.Model):
    follower = models.ForeignKey('users.User', models.DO_NOTHING)
    following = models.ForeignKey('users.User', models.DO_NOTHING, related_name='followers_following_set')
    followed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'followers'
        unique_together = (('follower', 'following'),)