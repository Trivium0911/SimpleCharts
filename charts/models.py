from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models



User = get_user_model()

class Chart(models.Model):
    objects = models.Manager()
    username = models.TextField(blank = True, default= 'username' )
    artist = models.TextField(blank = True, default= 'artist' )
    song_title = models.TextField(default="song")
    album = models.TextField(default="album", blank=True, null=True)
    date = models.TextField(default= 'date')
    date_utc = models.DateField(default=timezone.now)


    def __repr__(self):
        return f"{self.__class__.__name__}(username = {self.username}, artist = {self.artist}," \
               f" song_title = {self.song_title}, album = {self.album}, date = {self.date}"

    def get_absolute_url(self) -> str:
        return f"/charts/"