from django.db.models import Count
from django.shortcuts import render, redirect
from charts.models import Chart
from charts.last import pack_to_db, clear_user_db

chart = Chart.objects.all()

def get_user(request):
    user = request.user
    return user


def chart_list(request):
    cur_user = get_user(request)
    user_chart = chart.filter(username= cur_user)
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
        pack_to_db(cur_user)
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




def top_artists(request):
    cur_user = get_user(request)
    user_artists = chart.filter(username = cur_user)
    top_user_artists = user_artists.values('artist').annotate(count=Count('artist')).order_by("-count")
    return render(request,"charts/top_artists/1year.html",{"top_user_artists" : top_user_artists})