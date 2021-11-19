from django.urls import path
from charts.views import chart_list, top_artists_year, top_tracks_year, top_albums_year
from charts.views import download_user_db, delete_user_db



urlpatterns = [
    path("", chart_list, name="charts"),
    path("download", download_user_db, name="download"),
    path("delete", delete_user_db, name="delete"),
    path("artists_year",top_artists_year, name="artists_year"),
    path("tracks_year",top_tracks_year, name="tracks_year"),
    path("albums_year", top_albums_year, name="albums_year"),
]