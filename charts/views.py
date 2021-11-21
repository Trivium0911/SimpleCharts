from django.shortcuts import render, redirect
from pylast import PyLastError
from charts.models import Chart
from charts.last import pack_to_db, clear_user_db, get_user
from charts.last import get_top_artists, get_top_tracks, get_top_albums


chart = Chart.objects.all()


def chart_list(request):
    cur_user = get_user(request)
    user_chart = chart.filter(username = cur_user)
    if not user_chart:
        return render(request, 'charts/chart_list.html', { "no_charts": "You haven't charts"})
    first_date = user_chart.first()
    last_date = getattr(first_date, "date")
    return render(request, 'charts/chart_list.html', {"userchart": user_chart, "last_date": last_date })


def download_user_db(request):
    if request.method == "POST":
        cur_user = get_user(request)
        try:
            clear_user_db(cur_user)
        except AttributeError:
            pass
        try:
            pack_to_db(cur_user)
        except PyLastError:
            return redirect("charts")
        return redirect("charts")
    return render(request, "charts/download.html")


def delete_user_db(request):
    if request.method == "POST":
        cur_user = get_user(request)
        try:
            clear_user_db(cur_user)
        except AttributeError:
            return redirect("charts")
    return render (request,"charts/delete.html")




def top_artists_year(request):
    cur_user = get_user(request)
    period = 365
    top_artists_year = get_top_artists(cur_user,period)
    return render(request,"charts/top_artists/artists_year.html",{"top_artists_year" : top_artists_year})

def top_tracks_year(request):
    cur_user = get_user(request)
    period = 365
    top_tracks_year = get_top_tracks(cur_user,period)
    return render(request,"charts/top_tracks/tracks_year.html",{"top_tracks_year": top_tracks_year})

def top_albums_year(request):
    cur_user = get_user(request)
    period = 365
    top_albums_year = get_top_albums(cur_user,period)
    return render(request,"charts/top_albums/albums_year.html",{"top_albums_year" : top_albums_year})

def top_artists_6month(request):
    cur_user = get_user(request)
    period = 183
    top_artists_6month = get_top_artists(cur_user,period)
    return render(request,"charts/top_artists/artists_6month.html",{"top_artists_6month" : top_artists_6month})

def top_artists_3month(request):
    cur_user = get_user(request)
    period = 90
    top_artists_3month = get_top_artists(cur_user,period)
    return render(request,"charts/top_artists/artists_3month.html",{"top_artists_3month" : top_artists_3month})

def top_artists_month(request):
    cur_user = get_user(request)
    period = 30
    top_artists_month = get_top_artists(cur_user,period)
    return render(request,"charts/top_artists/artists_month.html",{"top_artists_month" : top_artists_month})

def top_artists_week(request):
    cur_user = get_user(request)
    period = 7
    top_artists_week = get_top_artists(cur_user,period)
    return render(request,"charts/top_artists/artists_week.html",{"top_artists_week" : top_artists_week})

def top_albums_6month(request):
    cur_user = get_user(request)
    period = 183
    top_albums_6month = get_top_albums(cur_user,period)
    return render(request,"charts/top_albums/albums_6month.html",{"top_albums_6month" : top_albums_6month})

def top_albums_3month(request):
    cur_user = get_user(request)
    period = 90
    top_albums_3month = get_top_albums(cur_user,period)
    return render(request,"charts/top_albums/albums_3month.html",{"top_albums_3month" : top_albums_3month})

def top_albums_month(request):
    cur_user = get_user(request)
    period = 30
    top_albums_month = get_top_albums(cur_user,period)
    return render(request,"charts/top_albums/albums_month.html",{"top_albums_month" : top_albums_month})

def top_albums_week(request):
    cur_user = get_user(request)
    period = 7
    top_albums_week = get_top_albums(cur_user,period)
    return render(request,"charts/top_albums/albums_week.html",{"top_albums_week" : top_albums_week})

def top_tracks_6month(request):
    cur_user = get_user(request)
    period = 183
    top_tracks_6month = get_top_tracks(cur_user,period)
    return render(request,"charts/top_tracks/tracks_6month.html",{"top_tracks_6month": top_tracks_6month})

def top_tracks_3month(request):
    cur_user = get_user(request)
    period = 90
    top_tracks_3month = get_top_tracks(cur_user,period)
    return render(request,"charts/top_tracks/tracks_3month.html",{"top_tracks_3month": top_tracks_3month})

def top_tracks_month(request):
    cur_user = get_user(request)
    period = 30
    top_tracks_month = get_top_tracks(cur_user,period)
    return render(request,"charts/top_tracks/tracks_month.html",{"top_tracks_month": top_tracks_month})

def top_tracks_week(request):
    cur_user = get_user(request)
    period = 7
    top_tracks_week = get_top_tracks(cur_user,period)
    return render(request,"charts/top_tracks/tracks_week.html",{"top_tracks_week": top_tracks_week})