from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from SimpleCharts.views import SignUpView, SimpleCharts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/charts/', include("charts.urls"), name = "charts"),
    path ("start/", SimpleCharts ,name='simplecharts'),
    path ("start/signup/", SignUpView.as_view(),name='signup'),
    path ("start/login/", LoginView.as_view(),name='login'),

]
