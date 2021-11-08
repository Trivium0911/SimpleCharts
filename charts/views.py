from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from charts.models import Chart
from charts.last import pack_to_db
from charts.last import lastfm_username

chart = Chart.objects.all()

class ChartView(ListView):
    model = Chart
    success_url = reverse_lazy('charts')


def download_user_db(request):
    if request.method == "POST":
        pack_to_db()
        return redirect("charts")
    return render(request, "charts/download.html")


def delete_user_db(request):
    if request.method == "POST":
        try:
            del_chart = Chart.objects.filter(username=lastfm_username)
            del_chart.delete()
            del_chart.save()
        except AttributeError:
            return redirect("charts")
    return render (request,"charts/delete.html")





