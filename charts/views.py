from django.shortcuts import render, redirect
from pylast import PyLastError
from charts.models import Chart
from charts.last import pack_to_db, clear_user_db, get_user, pagination, pack_to_db4, pack_to_db3, pack_to_db2
from charts.last import get_top_artists, get_top_tracks, get_top_albums



chart = Chart.objects.all()


def chart_list(request):
    cur_user = get_user(request)
    user_chart = chart.filter(username = cur_user)
    if not user_chart:
        return render(request, 'charts/chart_list.html', { "no_charts": "You haven't charts"})
    first_date = user_chart.first()
    last_date = getattr(first_date, "date")
    return render(request, 'charts/chart_list.html', { "last_date": last_date })


def download_user_db(request):
    cur_user = get_user(request)
    try:
        if request.method == "POST" and 'btnform1' in request.POST:
            pack_to_db(cur_user)
            return render(request, "charts/download.html")
        if request.method == "POST" and 'btnform2' in request.POST:
            pack_to_db2(cur_user)
            return render(request, "charts/download.html")
        if request.method == "POST" and 'btnform3' in request.POST:
            pack_to_db3(cur_user)
            return render(request, "charts/download.html")
        if request.method == "POST" and 'btnform4' in request.POST:
            pack_to_db4(cur_user)
            return render(request, "charts/download.html")
    except PyLastError:
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
    try:
        pages_artists_year = pagination(request,top_artists_year)
    except TypeError:
        return render(request, "charts/top_artists/artists_year.html")
    return render(request,"charts/top_artists/artists_year.html",{"pages_artists_year": pages_artists_year})

def top_tracks_year(request):
    cur_user = get_user(request)
    period = 365
    top_tracks_year = get_top_tracks(cur_user,period)
    try:
        pages_tracks_year = pagination(request, top_tracks_year)
    except TypeError:
        return render(request, "charts/top_tracks/tracks_year.html")
    return render(request, "charts/top_tracks/tracks_year.html", {"pages_tracks_year": pages_tracks_year})


def top_albums_year(request):
    cur_user = get_user(request)
    period = 365
    top_albums_year = get_top_albums(cur_user,period)
    try:
        pages_albums_year = pagination(request, top_albums_year)
    except TypeError:
        return render(request, "charts/top_albums/albums_year.html")
    return render(request, "charts/top_albums/albums_year.html", {"pages_albums_year": pages_albums_year})


def top_artists_6month(request):
    cur_user = get_user(request)
    period = 183
    top_artists_6month = get_top_artists(cur_user,period)
    try:
        pages_artists_6month = pagination(request,top_artists_6month)
    except TypeError:
        return render(request, "charts/top_artists/artists_6month.html")
    return render(request, "charts/top_artists/artists_6month.html", {"pages_artists_6month": pages_artists_6month})


def top_artists_3month(request):
    cur_user = get_user(request)
    period = 90
    top_artists_3month = get_top_artists(cur_user,period)
    try:
        pages_artists_3month = pagination(request, top_artists_3month)
    except TypeError:
        return render(request, "charts/top_artists/artists_3month.html")
    return render(request, "charts/top_artists/artists_3month.html", {"pages_artists_3month": pages_artists_3month})


def top_artists_month(request):
    cur_user = get_user(request)
    period = 30
    top_artists_month = get_top_artists(cur_user,period)
    try:
        pages_artists_month = pagination(request, top_artists_month)
    except TypeError:
        return render(request, "charts/top_artists/artists_month.html")
    return render(request,"charts/top_artists/artists_month.html",{"pages_artists_month" : pages_artists_month})

def top_artists_week(request):
    cur_user = get_user(request)
    period = 7
    top_artists_week = get_top_artists(cur_user,period)
    try:
        pages_artists_week = pagination(request, top_artists_week)
    except TypeError:
        return render(request, "charts/top_artists/artists_week.html")
    return render(request, "charts/top_artists/artists_week.html", {"pages_artists_week": pages_artists_week})


def top_albums_6month(request):
    cur_user = get_user(request)
    period = 183
    top_albums_6month = get_top_albums(cur_user,period)
    try:
        pages_albums_6month = pagination(request, top_albums_6month)
    except TypeError:
        return render(request, "charts/top_albums/albums_6month.html")
    return render(request, "charts/top_albums/albums_6month.html", {"pages_albums_6month": pages_albums_6month})

def top_albums_3month(request):
    cur_user = get_user(request)
    period = 90
    top_albums_3month = get_top_albums(cur_user,period)
    try:
        pages_albums_3month = pagination(request, top_albums_3month)
    except TypeError:
        return render(request, "charts/top_albums/albums_3month.html")
    return render(request, "charts/top_albums/albums_3month.html", {"pages_albums_3month": pages_albums_3month})

def top_albums_month(request):
    cur_user = get_user(request)
    period = 30
    top_albums_month = get_top_albums(cur_user,period)
    try:
        pages_albums_month = pagination(request, top_albums_month)
    except TypeError:
        return render(request, "charts/top_albums/albums_month.html")
    return render(request, "charts/top_albums/albums_month.html", {"pages_albums_month": pages_albums_month})

def top_albums_week(request):
    cur_user = get_user(request)
    period = 7
    top_albums_week = get_top_albums(cur_user,period)
    try:
        pages_albums_week = pagination(request, top_albums_week)
    except TypeError:
        return render(request, "charts/top_albums/albums_week.html")
    return render(request, "charts/top_albums/albums_week.html", {"pages_albums_week": pages_albums_week})

def top_tracks_6month(request):
    cur_user = get_user(request)
    period = 183
    top_tracks_6month = get_top_tracks(cur_user,period)
    try:
        pages_tracks_6month = pagination(request, top_tracks_6month)
    except TypeError:
        return render(request, "charts/top_tracks/tracks_6month.html")
    return render(request, "charts/top_tracks/tracks_6month.html", {"pages_tracks_6month": pages_tracks_6month})

def top_tracks_3month(request):
    cur_user = get_user(request)
    period = 90
    top_tracks_3month = get_top_tracks(cur_user,period)
    try:
        pages_tracks_3month = pagination(request, top_tracks_3month)
    except TypeError:
        return render(request, "charts/top_tracks/tracks_3month.html")
    return render(request, "charts/top_tracks/tracks_3month.html", {"pages_tracks_3month": pages_tracks_3month})

def top_tracks_month(request):
    cur_user = get_user(request)
    period = 30
    top_tracks_month = get_top_tracks(cur_user,period)
    try:
        pages_tracks_month = pagination(request, top_tracks_month)
    except TypeError:
        return render(request, "charts/top_tracks/tracks_month.html")
    return render(request, "charts/top_tracks/tracks_month.html", {"pages_tracks_month": pages_tracks_month})

def top_tracks_week(request):
    cur_user = get_user(request)
    period = 7
    top_tracks_week = get_top_tracks(cur_user,period)
    try:
        pages_tracks_week = pagination(request, top_tracks_week)
    except TypeError:
        return render(request, "charts/top_tracks/tracks_week.html")
    return render(request, "charts/top_tracks/tracks_week.html", {"pages_tracks_week": pages_tracks_week})

def last_listened(request):
    cur_user= get_user(request)
    user_chart = chart.filter(username=cur_user)
    try:
        pages_charts = pagination(request, user_chart)
    except TypeError:
        return render(request, "charts/top_albums/last_listened.html")
    return render(request, 'charts/last_listened.html', {"pages_charts": pages_charts})