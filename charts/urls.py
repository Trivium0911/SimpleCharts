from django.urls import path


from charts.views import ChartView

urlpatterns = [
    path("", ChartView.as_view(), )
]