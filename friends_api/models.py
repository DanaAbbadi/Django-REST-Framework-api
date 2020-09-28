from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Friends(models.Model):
    character = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    line      = models.CharField(max_length=64)
    plot      = models.CharField(max_length=64)
    episode   = models.CharField(max_length=64)
    season    = models.CharField(max_length=64)

    def __str__(self):
        return self.line
