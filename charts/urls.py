from django.urls import path
from charts.views import chart_list, last_listened
from charts.views import top_artists_year, top_artists_6month, top_artists_3month, top_artists_month, top_artists_week
from charts.views import top_albums_year, top_albums_6month, top_albums_3month, top_albums_month, top_albums_week
from charts.views import top_tracks_year, top_tracks_6month, top_tracks_3month, top_tracks_month, top_tracks_week
from charts.views import download_user_db, delete_user_db



urlpatterns = [
    path("", chart_list, name="charts"),
    path("download", download_user_db, name="download_user_db"),
    path("delete", delete_user_db, name="delete"),
    path("artists_year",top_artists_year, name="top_artists_year"),
    path("tracks_year",top_tracks_year, name="tracks_year"),
    path("albums_year", top_albums_year, name="albums_year"),
    path("artists_6month",top_artists_6month, name="top_artists_6month"),
    path("artists_3month",top_artists_3month, name="top_artists_3month"),
    path("artists_month",top_artists_month, name="top_artists_month"),
    path("artists_week",top_artists_week, name="top_artists_week"),
    path("albums_6month", top_albums_6month, name="albums_6month"),
    path("albums_3month", top_albums_3month, name="albums_3month"),
    path("albums_month", top_albums_month, name="albums_month"),
    path("albums_week", top_albums_week, name="albums_week"),
    path("tracks_6month", top_tracks_6month, name="tracks_6month"),
    path("tracks_3month", top_tracks_3month, name="tracks_3month"),
    path("tracks_month", top_tracks_month, name="tracks_month"),
    path("tracks_week", top_tracks_week, name="tracks_week"),
    path("last_listened", last_listened, name="last_listened"),

  


]