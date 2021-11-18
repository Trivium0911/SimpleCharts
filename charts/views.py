from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from charts.models import Chart
from charts.last import pack_to_db


chart = Chart.objects.all()

def get_user(request):
    user = request.user
    return user


def chart_list(request):
    cur_user = get_user(request)
    user_chart = chart.filter(username= cur_user)
    first_date = chart.first()
    if first_date is None:
        return render(request, 'charts/chart_list.html')
    last_date = getattr(first_date, "date")
    return render(request, 'charts/chart_list.html', {"userchart": user_chart, "last_date": last_date})


def download_user_db(request):
    if request.method == "POST":
        cur_user = get_user(request)
        pack_to_db(cur_user)
        return redirect("charts")
    return render(request, "charts/download.html")


def delete_user_db(request):
    cur_user = get_user(request)
    filter = chart.filter(username = cur_user)
    if request.method == "POST":
        try:
            del_chart = filter
            del_chart.delete()
            del_chart.save()
        except AttributeError:
            return redirect("charts")
    return render (request,"charts/delete.html")




