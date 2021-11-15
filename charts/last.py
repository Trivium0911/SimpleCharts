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
for i in User:
    print (i)
lastfm_username = os.getenv("lastfm_username")
lastfm_password_hash = pylast.md5(os.getenv("lastfm_password_hash"))
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
lastfm_network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=lastfm_username,
    password_hash=lastfm_password_hash,
)

date = round(datetime.datetime.today().timestamp())
past_date = datetime.datetime.today() - timedelta(days=365)
past_date = round(past_date.timestamp())
cur_user = int(LastFmProfile.objects.get(user=User))

def get_lastfm_data():
    top_list = lastfm_network.get_user(lastfm_username).get_recent_tracks(time_from=past_date, time_to=date, limit=None)
    return top_list


def pack_to_db():

    top_list = lastfm_network.get_user(lastfm_username).get_recent_tracks(time_from=past_date, time_to=date, limit=None)
    for top_item in top_list:
        date_utc = datetime.date.fromtimestamp(int(top_item.timestamp))
        # try:
        #     cur_name = LastFmProfile.objects.get(username=lastfm_username)
        # except:
        #     cur_name = LastFmProfile.objects.create(username=lastfm_username)
        chart = Chart(
           # username=cur_user,
            artist=top_item.track.artist,
            song_title=top_item.track.title,
            album=top_item.album,
            date=top_item.playback_date,
            date_utc=date_utc,
           # user = LastFmProfile.objects.get(User)
        )
        chart.save()
    return chart
