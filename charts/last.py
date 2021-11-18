import os
import pylast
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
from charts.models import Chart
from charts.models import LastFmProfile



datetime.datetime.now(tz=timezone.utc)

# LAST_FM_SETTINGS
User= get_user_model()

lastfm_username = os.getenv("lastfm_username")

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
lastfm_network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=lastfm_username#"maximbreakdown",
  # password_hash=lastfm_password_hash,
)

date = round(datetime.datetime.today().timestamp())
past_date = datetime.datetime.today() - timedelta(days=365)
past_date = round(past_date.timestamp())
#cur_user = int(LastFmProfile.objects.get(user=User))


def pack_to_db(cur_user):
    lastfm_network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET,
        username=cur_user,
    )

    top_list = lastfm_network.get_user(cur_user).get_recent_tracks(time_from=past_date, time_to=date, limit=None)
    for top_item in top_list:
        date_utc = datetime.date.fromtimestamp(int(top_item.timestamp))
        chart = Chart(
            username= cur_user,
            artist=top_item.track.artist,
            song_title=top_item.track.title,
            album=top_item.album,
            date=top_item.playback_date,
            date_utc=date_utc,

        )
        chart.save()
    return chart
