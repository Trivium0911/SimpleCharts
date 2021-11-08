from django.shortcuts import render
from django.views.generic import ListView
from charts.models import Chart
from charts.last import pack_to_db

from charts.models import LastFmProfile



from charts.last import lastfm_username

chart = Chart.objects.all()

class ChartView(ListView):
    model = Chart


def download_user_db(request):
    if request.method == "POST":
        pack_to_db()
        return render(request,"charts/download.html", {"download_user_db": pack_to_db()})
    return render(request, "charts/download.html")


def delete_user_db(request):
    if request.method == "POST":
        try:
            del_chart = Chart.objects.filter(username=lastfm_username)
            del_chart.delete()
            del_chart.save()
        except AttributeError:
            return render(request, "charts/delete.html",{"Done": f"db for {lastfm_username} cleared"})
    return render (request,"charts/delete.html")





