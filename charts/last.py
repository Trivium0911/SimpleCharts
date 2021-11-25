import os
import time
import pylast
from datetime import timedelta,datetime
from django.contrib.auth import get_user_model
import datetime
from django.core.paginator import Paginator
from django.db.models import Count
from charts.models import Chart


User = get_user_model()
chart = Chart.objects.all()
lastfm_username = os.getenv('lastfm_username')

# LAST_FM_SETTINGS
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
lastfm_network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username = lastfm_username
)

date = round(datetime.datetime.today().timestamp())
past_date = datetime.datetime.today() - timedelta(days=60)
past_date2 = past_date - timedelta(days=60)
past_date3 = past_date2 - timedelta(days=60)
past_date4 = past_date3 - timedelta(days=60)
past_date5 = past_date4 - timedelta(days=60)
past_date6 = past_date5 - timedelta(days=60)
year_date = past_date6
past_date = round(past_date.timestamp())
past_date2 = round( past_date2.timestamp())
past_date3 = round(past_date3.timestamp())
past_date4 = round( past_date4.timestamp())
past_date5 = round( past_date5.timestamp())
past_date6 = round( past_date6.timestamp())

def pagination(request,top):
    paginator = Paginator(top, 100)
    page_number = request.GET.get('page')
    obj = paginator.get_page(page_number)
    return obj

def datefilter(cur_user,period):
    user_charts = chart.filter(username=cur_user)
    if not user_charts:
        return None
    startdate = user_charts[0].date_utc
    enddate = startdate - timedelta(days=period)
    filtered_top = user_charts.filter(date_utc__range=[enddate, startdate])
    return filtered_top

def get_user(request):
    user = request.user
    return user

def clear_user_db(cur_user):
    del_chart = chart.filter(username=cur_user)
    del_chart.delete()
    del_chart.save()

def get_top_artists(cur_user,period):
    artists = datefilter(cur_user,period)
    if not artists:
        return None
    top_user_artists = artists.values('artist').annotate(count=Count('artist')).order_by("-count")
    return top_user_artists

def get_top_tracks(cur_user,period):
    tracks = datefilter(cur_user,period)
    if not tracks:
        return None
    top_user_tracks= tracks.values('artist', 'album','song_title').annotate(count=Count('song_title')).order_by("-count")
    return top_user_tracks

def get_top_albums(cur_user,period):
    albums = datefilter(cur_user,period)
    if not albums:
        return None
    top_user_albums = albums.values('artist', 'album').annotate(count=Count('album')).order_by("-count")
    return top_user_albums


def pack_to_db(cur_user):
    lastfm_network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET,
        username=cur_user,
    )
    top_list = lastfm_network.get_user(cur_user).get_recent_tracks(time_from = past_date, time_to=date, limit=None)
    if top_list == []:
        new_date = int(lastfm_network.get_user(cur_user).get_recent_tracks(limit=1)[0][3])
        new_past_date = str(datetime.date.fromtimestamp(new_date) - timedelta(days=60))
        new_past_date = int(time.mktime(time.strptime(new_past_date, '%Y-%m-%d')))
        top_list = lastfm_network.get_user(cur_user).get_recent_tracks(time_from=new_past_date, time_to=new_date,limit=None)
    for top_item in top_list:
        date_utc = datetime.date.fromtimestamp(int(top_item.timestamp))
        chart = Chart(
            username=cur_user,
            artist=top_item.track.artist,
            song_title=top_item.track.title,
            album=top_item.album,
            date=top_item.playback_date,
            date_utc=date_utc,
        )
        chart.save()
    return chart

def pack_to_db2(cur_user):
    lastfm_network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET,
        username=cur_user,
    )
    try:
        actual_date = chart.filter(username=cur_user)[0].date_utc
    except  IndexError:
        return None
    if actual_date > year_date.date():
        top_list = lastfm_network.get_user(cur_user).get_recent_tracks(time_from=past_date2, time_to=past_date,limit=None)
        for top_item in top_list:
            date_utc = datetime.date.fromtimestamp(int(top_item.timestamp))
            chart2 = Chart(
                username=cur_user,
                artist=top_item.track.artist,
                song_title=top_item.track.title,
                album=top_item.album,
                date=top_item.playback_date,
                date_utc=date_utc,

              )
            chart2.save()
        return chart2



def pack_to_db3(cur_user):
    lastfm_network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET,
        username=cur_user,
    )
    try:
        actual_date = chart.filter(username=cur_user)[0].date_utc
    except  IndexError:
        return None
    if actual_date > year_date.date():
        top_list = lastfm_network.get_user(cur_user).get_recent_tracks(time_from=past_date3, time_to=past_date2, limit=None)
        for top_item in top_list:
            date_utc = datetime.date.fromtimestamp(int(top_item.timestamp))
            chart3 = Chart(
                username=cur_user,
                artist=top_item.track.artist,
                song_title=top_item.track.title,
                album=top_item.album,
                date=top_item.playback_date,
                date_utc=date_utc,

            )
            chart3.save()
        return chart3


def pack_to_db4(cur_user):
    lastfm_network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET,
        username=cur_user,
    )
    try:
        actual_date = chart.filter(username=cur_user)[0].date_utc
    except  IndexError:
        return None
    if actual_date > year_date.date():
        top_list = lastfm_network.get_user(cur_user).get_recent_tracks(time_from=past_date4, time_to=past_date3, limit=None)
        for top_item in top_list:
            date_utc = datetime.date.fromtimestamp(int(top_item.timestamp))
            chart4 = Chart(
                username=cur_user,
                artist=top_item.track.artist,
                song_title=top_item.track.title,
                album=top_item.album,
                date=top_item.playback_date,
                date_utc=date_utc,
            )
            chart4.save()
        return chart4

def pack_to_db5(cur_user):
    lastfm_network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET,
        username=cur_user,
    )
    try:
        actual_date = chart.filter(username=cur_user)[0].date_utc
    except  IndexError:
        return None
    if actual_date > year_date.date():
        top_list = lastfm_network.get_user(cur_user).get_recent_tracks(time_from=past_date5, time_to=past_date4, limit=None)
        for top_item in top_list:
            date_utc = datetime.date.fromtimestamp(int(top_item.timestamp))
            chart5 = Chart(
                username=cur_user,
                artist=top_item.track.artist,
                song_title=top_item.track.title,
                album=top_item.album,
                date=top_item.playback_date,
                date_utc=date_utc,
            )
            chart5.save()
        return chart5

def pack_to_db6(cur_user):
    lastfm_network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET,
        username=cur_user,
    )
    try:
        actual_date = chart.filter(username=cur_user)[0].date_utc
    except  IndexError:
        return None
    if actual_date > year_date.date():
        top_list = lastfm_network.get_user(cur_user).get_recent_tracks(time_from=past_date6, time_to=past_date5, limit=None)
        for top_item in top_list:
            date_utc = datetime.date.fromtimestamp(int(top_item.timestamp))
            chart6 = Chart(
                username=cur_user,
                artist=top_item.track.artist,
                song_title=top_item.track.title,
                album=top_item.album,
                date=top_item.playback_date,
                date_utc=date_utc,
            )
            chart6.save()
        return chart6