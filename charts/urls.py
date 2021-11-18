from django.urls import path
from charts.views import chart_list, top_artists
from charts.views import download_user_db, delete_user_db



urlpatterns = [
    path("", chart_list, name="charts"),
    path("download/", download_user_db, name="download"),
    path("delete/", delete_user_db, name="delete"),
    path("artists_1year",top_artists, name="top_artists_1year"),

]