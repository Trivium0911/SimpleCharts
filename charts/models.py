from django.contrib.auth import get_user_model
from django.db import models
import pylast

User = get_user_model()


class LastFmProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,)
    username = models.TextField
    password = models.TextField()

    def __repr__(self):
        return f"{self.__class__.__name__}(username = {self.username}, password= {self.password})"

class Chart(models.Model):
    info = models.TextField(unique=True)
    count = models.TextField(unique=True,null=False,default=0)
