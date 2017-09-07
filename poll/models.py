from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=200)
    score = models.IntegerField()
    create_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
		return self.user_name