# Create your views here.
# from SimpleCharts.settings import lastfm_network, lastfm_username
# from charts.models import Chart
#

from django.views.generic import ListView
from charts.models import Chart

chart = Chart.objects.all()

class ChartView(ListView):
    model = Chart
#     pack_to_db()
#     chart_top_10 = Chart.objects.order_by()[:10]
#     #delete_user_data()
#     return render(request,'charts/charts.html',{'n':chart_top_10} ) #{'done': 'done'})#
# # #
# # #
# #     return HttpResponse(chart)
#
#
# def track_and_timestamp(track):
#     return f"{track.playback_date}\t{track.track}"
#
#
# def print_track(track):
#     print(track_and_timestamp(track))
#
# # top_list = lastfm_network.get_user(lastfm_username).get_top_artists(period='12month', limit=20)
# def show(request:HttpRequest):
#     top_list = lastfm_network.get_user(lastfm_username).get_top_artists(period='12month', limit=100)
#     chart = Chart()
#     for top_item in top_list:
#         item = top_item.item
#         chart = Chart(
#             username = lastfm_username,
#             artist =item.name,
#             count=int(top_item.weight),
#         )
#         chart.save()
#     return HttpResponse(f"{chart}")


